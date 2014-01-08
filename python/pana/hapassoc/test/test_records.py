import os
from pana.hapassoc.records import HapAssocResRec
from pana.hapassoc.test.template import SafeHapAssocTester


class TestHapAssocResRec(SafeHapAssocTester):

    def __init__(self, test_name):
        SafeHapAssocTester.__init__(self, test_name)

    def setUp(self):
        self.test_class = 'HapAssocResRec'

#    def __create_model_instance(self):
#        model = SummarizeAnnovarHapAssoc()
#        return model

    def test_default(self):
        """

        to check if haplotype association result record is correctly load

        """

        self.init_test(self.current_func_name)

        case1_found = False
        case2_found = False
        test_file_name = self.full_path(self.current_func_name + '.txt')
        test_file = open(test_file_name)
        for line in test_file:
            rec = HapAssocResRec(line.strip().split())
            if (rec.locus == 'WIN4') and (rec.haplotype == 'G'):
                case1_found = True
                self.assertEqual(rec.f_a,
                                 0.04025,
                                 'Invalid cases frequency')
                self.assertEqual(rec.f_u,
                                 0.03,
                                 'Invalid controls frequency')
                self.assertEqual(rec.chisq,
                                 0.8336,
                                 'Invalid chisq')
                self.assertEqual(rec.p_value,
                                 0.3612,
                                 'Invalid p value')
                self.assertEqual(rec.snps,
                                 'rs16910109',
                                 'Invalid SNPS')
            if (rec.locus == 'WIN11268') and (rec.haplotype == 'GGAAAGAGAGCAAAAGGGCGCCAAGAAGAAAAGAAAAAGGCAGAGCAGGG'):
                case2_found = True
                self.assertEqual(rec.f_a,
                                 0.03822,
                                 'Invalid cases frequency')
                self.assertEqual(rec.f_u,
                                 0.04293,
                                 'Invalid controls frequency')
                self.assertEqual(rec.chisq,
                                 0.1076,
                                 'Invalid chisq')
                self.assertEqual(rec.p_value,
                                 0.7429,
                                 'Invalid p value')
                self.assertEqual(rec.snps,
                                 'rs10820282|rs7854657|rs10990317|rs12551330|rs7869941|rs12376672|rs10217639|rs7848024|rs13294991|rs1552766|rs7866606|rs7033449|rs2812594|rs10990353|rs1492598|rs10512305|rs16922214|rs4742861|rs843270|rs10990359|rs10990361|rs843283|rs1352979|rs2220706|rs843275|rs843272|rs1492600|rs10990362|rs11496631|rs10990381|rs10990384|rs1935861|rs10124970|rs2067711|rs10820319|rs12005200|rs10820320|rs4409450|rs12000047|rs2211427|rs10990402|rs10990405|rs1934995|rs10124146|rs1341204|rs12156626|rs10990416|rs10760932|rs10990423|rs10990424',
                                 'Invalid SNPS')
        self.assertTrue(case1_found,
                        'First case is not found')
        self.assertTrue(case2_found,
                        'Second case is not found')

    def test_or(self):
        """ to check if the estimated odd ratio is calculated correctly """

        self.init_test(self.current_func_name)

        case1_found = False
        case2_found = False
        case3_found = False
        case4_found = False
        test_file_name = self.full_path(self.current_func_name + '.txt')
        test_file = open(test_file_name)
        for line in test_file:
            rec = HapAssocResRec(line.strip().split())
            if (rec.locus == 'WIN98') and (rec.haplotype == 'C'):
                case1_found = True
                self.assertEqual(round(rec.or_value, 4),
                                 3.1040,
                                 'Invalid odd ratio')
            if (rec.locus == 'WIN4021') and (rec.haplotype == 'CAGGA'):
                case2_found = True
                self.assertEqual(round(rec.or_value, 4),
                                 3.1847,
                                 'Invalid odd ratio')
            if (rec.locus == 'WIN7616') and (rec.haplotype == 'CGGGAGGGGGAAGAGGGGGA'):
                case3_found = True
                self.assertEqual(round(rec.or_value, 4),
                                 3.1595,
                                 'Invalid odd ratio')
            if (rec.locus == 'WIN11202') and (rec.haplotype == 'GGGCAAGGAGGAGAGAGACGAAAAGGGCAGGAAAGAGGAGAGAGAGGAAA'):
                case4_found = True
                self.assertEqual(round(rec.or_value, 4),
                                 3.1180,
                                 'Invalid odd ratio')
        self.assertTrue(case1_found,
                        'First case is not found')
        self.assertTrue(case2_found,
                        'Second case is not found')
        self.assertTrue(case3_found,
                        'Third case is not found')
        self.assertTrue(case4_found,
                        'Forth case is not found')

    def test_valid_window(self):
        """ to check if the record validation is correctly computed """

        self.init_test(self.current_func_name)

        case1_found = False
        case2_found = False
        case3_found = False
        case4_found = False
        case5_found = False
        case6_found = False
        case7_found = False
        test_file_name = self.full_path(self.current_func_name + '.txt')
        test_file = open(test_file_name)
        for line in test_file:
            rec = HapAssocResRec(line.strip().split())
            if (rec.locus == 'WIN98') and (rec.haplotype == 'C'):
                case1_found = True
                self.assertTrue(rec.valid_window,
                                'Invalid window validation')
            if (rec.locus == 'WIN98') and (rec.haplotype == 'A'):
                case2_found = True
                self.assertFalse(rec.valid_window,
                                 'Invalid window validation')
            if (rec.locus == 'WIN4021') and (rec.haplotype == 'OMNIBUS'):
                case3_found = True
                self.assertFalse(rec.valid_window,
                                 'Invalid window validation')
            if (rec.locus == 'WIN4021') and (rec.haplotype == 'CGGGA'):
                case4_found = True
                self.assertFalse(rec.valid_window,
                                 'Invalid window validation')
            if (rec.locus == 'WIN9157') and (rec.haplotype == 'GGGGGGCAAGAACAGGAAAG'):
                case5_found = True
                self.assertFalse(rec.valid_window,
                                 'Invalid window validation')
            if (rec.locus == 'WIN11202') and (rec.haplotype == 'GGGCAAGGAGGAGAGAGACGAAAAGGGCAGGAAAGAGGAGAGAGAGGAAA'):
                case6_found = True
                self.assertTrue(rec.valid_window,
                                'Invalid window validation')
#            if (rec.locus == 'WIN7616') and (rec.haplotype == 'CGGGAGGGGGAAGAGGGGGA'):
#                case3_found = True
#                self.assertEqual(round(rec.or_value, 4),
#                                 3.1595,
#                                 'Invalid odd ratio')
#            if (rec.locus == 'WIN11202') and (rec.haplotype == 'GGGCAAGGAGGAGAGAGACGAAAAGGGCAGGAAAGAGGAGAGAGAGGAAA'):
#                case4_found = True
#                self.assertEqual(round(rec.or_value, 4),
#                                 3.1180,
#                                 'Invalid odd ratio')
        self.assertTrue(case1_found,
                        'First case is not found')
        self.assertTrue(case2_found,
                        'Second case is not found')
        self.assertTrue(case3_found,
                        'Third case is not found')
        self.assertTrue(case4_found,
                        'Forth case is not found')
        self.assertTrue(case5_found,
                        'Fifth case is not found')
        self.assertTrue(case6_found,
                        'Sixth case is not found')


#    def test_init_custom(self):
#        """ to check if SOMBase initialize correctly (custom) """
#
#        self.init_test(self.current_func_name)
#        model = SOMBase(200,
#                        weight_step_size=0.3,
#                        nbh_step_size=3,
#                        map_size=100,
#                        max_nbh_size=70,
#                        random_seed=TEST_SEED
#                        )
#        self.assertEqual(model.features_size,
#                         200,
#                         'Incorrect number of features')
#        self.assertEqual(model.map_size,
#                         100,
#                         'Incorrect size of model mapping')
#        self.assertEqual(model.weight_step_size,
#                         0.3,
#                         'Incorrect weight step size')
#        self.assertEqual(model.nbh_step_size,
#                         3,
#                         'Incorrect neighbor hoods step size')
#        self.assertEqual(model.max_nbh_size,
#                         70,
#                         'Incorrect maximum number of neighborhood')
#        self.assertEqual(model.random_seed,
#                         20,
#                         'Invalid random seed')
#
#    def test_init_random_weight_map(self):
#        """ to check if SOMBase initialize random weight_map correctly """
#
#        self.init_test(self.current_func_name)
#        model = SOMBase(5,
#                        random_seed=TEST_SEED
#                        )
#        self.assertEqual(round(model.weight_map[0][1], 4),
#                         0.8977,
#                         'Invalid random weight map')
#
#    def test_nbhs(self):
#        """ to check if the function can correctly locate neighborhoods """
#
#        self.init_test(self.current_func_name)
#        model = SOMBase(5,
#                        map_size=5,
#                        random_seed=TEST_SEED
#                        )
#        self.assertEqual(list(model.nbhs(3, 2)),
#                         [1, 2, 3, 4],
#                         'Invalid neighbors')
#        self.assertEqual(list(model.nbhs(0, 1)),
#                         [0, 1],
#                         'Invalid neighbors')
#
#    def test_nbh_range(self):
#        """ to check if the function can correctly generate numbber of nbh """
#
#        self.init_test(self.current_func_name)
#        model = SOMBase(5,
#                        map_size=5,
#                        max_nbh_size=9,
#                        nbh_step_size=2,
#                        )
#        self.assertEqual(list(model.nbh_range()),
#                         [9, 7, 5, 3, 1],
#                         'Invalid neighbor range')
#        model = SOMBase(20,
#                        map_size=20,
#                        max_nbh_size=3,
#                        nbh_step_size=1,
#                        )
#        self.assertEqual(list(model.nbh_range()),
#                         [3, 2, 1, 0],
#                         'Invalid neighbor range')
#        model = SOMBase(20,
#                        map_size=20,
#                        max_nbh_size=3,
#                        nbh_step_size=0.7,
#                        )
#        self.assertEqual(map(lambda x: round(x, 1), list(model.nbh_range())),
#                         [3, 2.3, 1.6, 0.9, 0.2],
#                         'Invalid neighbor range')
#
#    def test_train(self):
#        """ to see if SOMBase can correctly train testing toy samples """
#
#        self.init_test(self.current_func_name)
#
#        animals = pana.plugin.toy.animal.load_animals()
#        prop_size = len(animals[0].features)
#        model = SOMBase(prop_size,
#                        random_seed=TEST_SEED,
#                        max_nbh_size=40,
#                        nbh_step_size=1,
#                        map_size=100,
#                        )
#        model.train(animals)
#        test_sample = animals[4]
#        winner, diff = model.calc_similarity(test_sample.features)
#        self.assertEqual(test_sample.name,
#                         'beetle',
#                         'Invalid sample name')
#        self.assertEqual(winner,
#                         95,
#                         'Invalid winner node')
#        test_sample = animals[12]
#        winner, diff = model.calc_similarity(test_sample.features)
#        self.assertEqual(test_sample.name,
#                         'elephant',
#                         'Invalid sample name')
#        self.assertEqual(winner,
#                         18,
#                         'Invalid winner node')
#
#
#class TestSOM2D(SafeHapAssocTester):
#
#    def __init__(self, test_name):
#        SafeHapAssocTester.__init__(self, test_name)
#
#    def setUp(self):
#        self.test_class = 'Som2D'
#
#    def test_init_default(self):
#        """ to check if SOM2D initialize correctly (default) """
#
#        self.init_test(self.current_func_name)
#        model = SOM2D(5)
#        self.assertEqual(model.features_size,
#                         5,
#                         'Incorrect number of features')
#        self.assertEqual(model.map_size,
#                         DFLT_MAP_ROWS*DFLT_MAP_COLS,
#                         'Incorrect size of model mapping')
#        self.assertEqual(model.weight_step_size,
#                         DFLT_WEIGHT_STEP_SIZE,
#                         'Incorrect step size')
#        self.assertEqual(model.max_nbh_size,
#                         DFLT_MAX_NBH_SIZE,
#                         'Incorrect maximum number of neighborhood')
#
#    def test_to_grid(self):
#        """ to check if SOM2D can transform indices to 2D positions """
#
#        self.init_test(self.current_func_name)
#        model = SOM2D(5,
#                      map_rows=5,
#                      map_cols=4,
#                      )
#        test_row, test_col = model.to_grid(5)
#        self.assertEqual(test_row,
#                         0,
#                         'Incorrect 2D row')
#        self.assertEqual(test_col,
#                         1,
#                         'Incorrect 2D col')
#        test_row, test_col = model.to_grid(9)
#        self.assertEqual(test_row,
#                         4,
#                         'Incorrect 2D row')
#        self.assertEqual(test_col,
#                         1,
#                         'Incorrect 2D col')
#        test_row, test_col = model.to_grid(11)
#        self.assertEqual(test_row,
#                         1,
#                         'Incorrect 2D row')
#        self.assertEqual(test_col,
#                         2,
#                         'Incorrect 2D col')
#        test_row, test_col = model.to_grid(19)
#        self.assertEqual(test_row,
#                         4,
#                         'Incorrect 2D row')
#        self.assertEqual(test_col,
#                         3,
#                         'Incorrect 2D col')
#
#    def test_from_grid(self):
#        """ to check if SOM2D can transform 2D positions to indices """
#
#        self.init_test(self.current_func_name)
#        model = SOM2D(5,
#                      map_rows=7,
#                      map_cols=3,
#                      )
#        test_row = 3
#        test_col = 2
#        test_idx = model.from_grid(test_row, test_col)
#        self.assertEqual(test_idx,
#                         17,
#                         'Incorrect idx')
#        test_row = 4
#        test_col = 1
#        test_idx = model.from_grid(test_row, test_col)
#        self.assertEqual(test_idx,
#                         11,
#                         'Incorrect idx')
#
#    def test_to_from_grid(self):
#        """ to check if SOM2D can transform between 2D positions to indices """
#
#        self.init_test(self.current_func_name)
#        model = SOM2D(5,
#                      map_rows=6,
#                      map_cols=2,
#                      )
#        test_row = 3
#        test_col = 1
#        test_idx = model.from_grid(test_row, test_col)
#        out_row, out_col = model.to_grid(test_idx)
#        self.assertEqual(out_row,
#                         3,
#                         'Incorrect 2D row')
#        self.assertEqual(out_col,
#                         1,
#                         'Incorrect 2D col')
#        test_idx = 5
#        test_row, test_col = model.to_grid(test_idx)
#        out_idx = model.from_grid(test_row, test_col)
#        self.assertEqual(out_idx,
#                         5,
#                         'Incorrect idx')
#
#    def test_nbhs2D(self):
#        """ to check if the function can locate 2D neighborhoods """
#
#        self.init_test(self.current_func_name)
#        model = SOM2D(5,
#                      map_rows=8,
#                      map_cols=9,
#                      random_seed=TEST_SEED
#                      )
#        nbh_indices = list(model.nbhs(42, 3))
#        self.assertEqual(23 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(24 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(25 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(26 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(27 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(28 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(29 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(60 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(61 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(17 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(18 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(45 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(53 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(len(nbh_indices),
#                         28,
#                         'Incorrect number of neighborhoods')
#        nbh_indices = list(model.nbhs(42, 4))
#        self.assertEqual(10 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(20 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(21 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(22 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(23 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(46 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(len(nbh_indices),
#                         42,
#                         'Incorrect number of neighborhoods')
#        nbh_indices = list(model.nbhs(42, 3.9))
#        self.assertEqual(10 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(20 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(21 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(22 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(23 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(46 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(len(nbh_indices),
#                         40,
#                         'Incorrect number of neighborhoods')
#        nbh_indices = list(model.nbhs(29, 1))
#        self.assertEqual(28 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(29 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(30 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(21 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(37 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(len(nbh_indices),
#                         5,
#                         'Incorrect number of neighborhoods')
#        nbh_indices = list(model.nbhs(32, 0))
#        self.assertEqual(32 in nbh_indices,
#                         True,
#                         'Incorrect neighborhood')
#        self.assertEqual(33 in nbh_indices,
#                         False,
#                         'Incorrect neighborhood')
#        self.assertEqual(len(nbh_indices),
#                         1,
#                         'Incorrect number of neighborhoods')
