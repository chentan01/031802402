import unittest
from test import SimilarityCalculate

class SimilarityTest (unittest.TestCase):

    def test_add (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1=fp.read()
        with open("D:\\sim_0.8\\orig_0.8_add.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_add.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_mix (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_mix.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_mix.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_del (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_del.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_del.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_rep(self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_rep.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_rep.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_dis_1 (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_dis_1.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_dis_1.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_dis_3 (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_dis_3.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_dis_3.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_dis_7 (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_dis_7.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_dis_7.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_dis_10 (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_dis_10.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_dis_10.txt的相似度")
        SimilarityCalculate(test_1, test_2)

    def test_dis_15 (self):
        with open("D:\\sim_0.8\\orig.txt", "r", encoding='utf-8') as fp:
            test_1 = fp.read()
        with open("D:\\sim_0.8\\orig_0.8_dis_15.txt", "r", encoding='utf-8') as fp:
            test_2 = fp.read()
        print("orig.txt与orig_0.8_dis_15.txt的相似度")
        SimilarityCalculate(test_1, test_2)


if __name__ == '__main__':

    unittest.main()
