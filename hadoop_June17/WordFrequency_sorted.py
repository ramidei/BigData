from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word.lower(), 1

    def reducer(self, key, values):
        yield str(sum(values)).zfill(6), key

    
if __name__ == '__main__':
    MRWordFrequencyCount.run()
