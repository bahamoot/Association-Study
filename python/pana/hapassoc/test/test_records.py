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
