import json
import random
import pandas as pd
from deap import base, tools, creator, algorithms

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.day_data = None
        self.df_ovens = None
        self.df_series = None

    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.day_data = json.load(file)

    def analyze_day(self, day):
        self.df_ovens = pd.DataFrame(self.day_data['ovens'])
        self.df_series = pd.DataFrame(self.day_data['series'])

        self.df_ovens['day'] = day
        self.df_series['day'] = day

        print("Средняя начальная температура печей:", self.df_ovens['start_temp'].mean())
        print("Минимальная температура серий:", self.df_series['temperature'].min())

class GeneticAlgorithm:
    def __init__(self, df_ovens, df_series):
        self.df_ovens = df_ovens
        self.df_series = df_series

        creator.create("Fitness", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.Fitness)
        self.toolbox = base.Toolbox()
        self.toolbox.register("individual", self.individual_from_series_operations, df_series=df_series, df_ovens=df_ovens)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        self.toolbox.register("select", tools.selTournament, tournsize=3)
        self.toolbox.register("evaluate", self.evaluate)

    def individual_from_series_operations(self, df_series, df_ovens):
        exploded_series = df_series['operations'].explode()
        unique_operations = set(json.dumps(d, sort_keys=True) for d in exploded_series)

        unique_operations_as_strings = [json.dumps(d, sort_keys=True) for d in unique_operations]

        all_unique_operations = list(set(unique_operations_as_strings))

        operation_indices = {op_str: idx for idx, op_str in enumerate(all_unique_operations)}

        unique_ovens = tuple(df_ovens.index)
        ind_size = len(all_unique_operations) * len(unique_ovens)

        ind = creator.Individual()
        ind.genotype = [random.choice(list(operation_indices.values())) for _ in range(ind_size)]
        ind.operation_indices = operation_indices
        ind.unique_ovens = unique_ovens

        return ind

    def evaluate(self, ind):
        genotype = ind.genotype
        operation_indices = ind.operation_indices
        unique_ovens = ind.unique_ovens

        df_individual = pd.DataFrame(index=self.df_series.index, columns=self.df_ovens.index, data=0)

        for i, value in enumerate(genotype):
            operation = list(operation_indices.keys())[i % len(operation_indices)]
            oven = unique_ovens[i // len(operation_indices)]

            # Skip non-numeric values
            if not isinstance(df_individual.loc[oven, df_individual.columns[i % len(self.df_ovens)]], (int, float)):
                continue

            df_individual.loc[oven, df_individual.columns[i % len(self.df_ovens)]] = value

        fitness = 0

        for index, row in self.df_series.iterrows():
            temperature = row['temperature']
            operations = row.get('operations', [])

            for operation in operations:
                if df_individual.loc[index, df_individual.loc[index] > 0].any():
                    oven_id = df_individual.loc[index].idxmax()
                    # Convert oven_id to integer before using it as an index
                    oven_id = int(oven_id)
                    fitness += self.df_ovens.loc[oven_id, 'start_temp']

        return (fitness,)

    def run_genetic_algorithm(self):
        population = [self.toolbox.individual() for _ in range(50)]

        for ind in population:
            ind.fitness.values = self.toolbox.evaluate(ind)

        algorithms.eaMuPlusLambda(population, self.toolbox, mu=50, lambda_=200, cxpb=0.7, mutpb=0.2, ngen=100, stats=None, halloffame=None, verbose=True)

        best_individual = tools.selBest(population, k=1)[0]
        print("Лучшая индивидуальная оценка:", best_individual.fitness.values[0])

if __name__ == "__main__":
    file_path = "example/day-3.json"
    day_to_optimize = 0

    data_processor = DataProcessor(file_path)
    data_processor.read_json()
    data_processor.analyze_day(day_to_optimize)

    genetic_algorithm = GeneticAlgorithm(data_processor.df_ovens, data_processor.df_series)
    genetic_algorithm.run_genetic_algorithm()
