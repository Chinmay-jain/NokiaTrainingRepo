import abc


class LNHOIF:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):

        LNHOIF.parameter_list['frequncy'] = frequency


class IRFIM:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):
        IRFIM.parameter_list['frequncy'] = frequency


class LNHOW:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):
        LNHOW.parameter_list['frequncy'] = frequency


class UFFIM:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):
        UFFIM.parameter_list['frequncy'] = frequency


class LNHOG:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):
        LNHOG.parameter_list['frequncy'] = frequency


class GFIM:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):
        GFIM.parameter_list['frequncy'] = frequency


class REDRT:
    dn = ''
    parameter_list = {}

    def __init__(self, frequency):
        REDRT.parameter_list['frequncy'] = frequency


class AbstractFactory:
    __metaclass__ = abc.ABCMeta

    def getMO(self, technology, frequency):
        pass

    @abc.abstractmethod
    def getMO_DN(self,technology,frequency):
        pass

    @abc.abstractmethod
    def getMO_Attributes(self,technology,frequency):
        pass


class LTE_ANR_Specification_Rules:
    neighbour_list = [2300, 2320, 2340, 1800, 1820, 1840, 1600, 1620, 1640]
    add = {}
    update = {}
    delete = {}
    managed_object = {}
    managed_object['add'] = add
    managed_object['update'] = update
    managed_object['delete'] = delete

    def run(self):
        frequency_seperator = FrequencySeperator()
        lte_frequency_list, wcdma_frequency_list, gsm_frequency_list = FrequencySeperator.seperateFrequencies(frequency_seperator, LTE_ANR_Specification_Rules.neighbour_list)

        lte_factory = LTEFactory()
        wcdma_factory = WCDMAFactory()
        gsm_factory = GSMFactory()

        return LTEFactory.getMO(lte_factory,'LTE',lte_frequency_list), WCDMAFactory.getMO(wcdma_factory,'WCDMA',wcdma_frequency_list), GSMFactory.getMO(gsm_factory,'GSM',gsm_frequency_list)


class FrequencySeperator:
    lte_frequency_list = []
    wcdma_frequency_list = []
    gsm_frequency_list = []

    def seperateFrequencies(self, neighbour_list):
        for neighbour in neighbour_list:
            if neighbour < 1800:
                FrequencySeperator.gsm_frequency_list.append(neighbour)
            elif neighbour < 2300:
                FrequencySeperator.wcdma_frequency_list.append(neighbour)
            else:
                FrequencySeperator.lte_frequency_list.append(neighbour)
        return FrequencySeperator.lte_frequency_list, FrequencySeperator.wcdma_frequency_list, FrequencySeperator.gsm_frequency_list


class LTEFactory(AbstractFactory):
    lte_objects = []

    def getMO(self, technology, frequency_list):
        for frequency in frequency_list:
            return LTEFactory.getMO_DN(LTEFactory(),technology,frequency), LTEFactory.getMO_Attributes(LTEFactory(),technology,frequency)

    def getMO_DN(self,technology,frequency):
        LTE_ANR_Specification_Rules.add['LNHOIF '+frequency] = {}
        LTE_ANR_Specification_Rules.add['IRFIM '+frequency] = {}
        LTE_ANR_Specification_Rules.add['REDRT '+frequency] = {}

        # lnhoif, irfim, redrt = LNHOIF(frequency), IRFIM(frequency), REDRT(frequency)
        # lnhoif.dn, irfim.dn, redrt.dn = 'LNHOIF '+frequency, 'IRFIM '+frequency, 'REDRT '+frequency


    def getMO_Attributes(self,technology,frequency):
        return LNHOIF,IRFIM.parameter_list,REDRT.parameter_list


class WCDMAFactory(AbstractFactory):
    wcdma_objects = []

    def getMO(self, technology, frequency_list):
        for frequency in frequency_list:
            return WCDMAFactory.getMO_DN(WCDMAFactory(),technology,frequency), WCDMAFactory.getMO_Attributes(WCDMAFactory(),technology,frequency)

    def getMO_DN(self,technology,frequency):
        return LNHOW(frequency),UFFIM(frequency),REDRT(frequency)

    def getMO_Attributes(self,technology,frequency):
        return LNHOW.parameter_list,UFFIM.parameter_list,REDRT.parameter_list


class GSMFactory(AbstractFactory):
    gsm_objects = []

    def getMO(self, technology, frequency_list):
        for frequency in frequency_list:
            return GSMFactory.getMO_DN(GSMFactory(),technology,frequency), GSMFactory.getMO_Attributes(GSMFactory(),technology,frequency)

    def getMO_DN(self,technology,frequency):
        return LNHOG(frequency),GFIM(frequency),REDRT(frequency)

    def getMO_Attributes(self,technology,frequency):
        return LNHOG.parameter_list,GFIM.parameter_list,REDRT.parameter_list


print LTE_ANR_Specification_Rules.main(LTE_ANR_Specification_Rules())

# kk = FrequencySeperator()
# FrequencySeperator.generateMOsForFrequency(kk)

