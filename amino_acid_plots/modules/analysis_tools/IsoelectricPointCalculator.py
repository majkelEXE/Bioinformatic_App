class IsoelectricPoint:
    def __init__(self):
        self.scale = {'Cterm': 2.869, 'pKAsp': 3.872, 'pKGlu': 4.412, 'pKCys': 7.555, 'pKTyr': 10.85,  'pk_his': 5.637, 'Nterm': 9.094, 'pKLys': 9.052,  'pKArg': 11.84}    # IPC protein 
        self.pKcterminal = {'D': 4.55, 'E': 4.75} 
        self.pKnterminal = {'A': 7.59, 'M': 7.0, 'S': 6.93, 'P': 8.36, 'T': 6.82, 'V': 7.44, 'E': 7.7}
        

    def calc_isoelectric_point(self, seq):
        pH = 6.51             
        pHprev = 0.0         
        pHnext = 14.0        
        E = 0.01             
        temp = 0.01

        while 1:            
            QN1=-1.0/(1.0+pow(10,(self.scale['Cterm']-pH)))                                        
            QN2=-seq.count('D')/(1.0+pow(10,(self.scale['pKAsp']-pH)))           
            QN3=-seq.count('E')/(1.0+pow(10,(self.scale['pKGlu']-pH)))           
            QN4=-seq.count('C')/(1.0+pow(10,(self.scale['pKCys']-pH)))           
            QN5=-seq.count('Y')/(1.0+pow(10,(self.scale['pKTyr']-pH)))        
            QP1=seq.count('H')/(1.0+pow(10,(pH-self.scale['pk_his'])))            
            QP2=1.0/(1.0+pow(10,(pH-self.scale['Nterm'])))                
            QP3=seq.count('K')/(1.0+pow(10,(pH-self.scale['pKLys'])))           
            QP4=seq.count('R')/(1.0+pow(10,(pH-self.scale['pKArg'])))            
            NQ=QN1+QN2+QN3+QN4+QN5+QP1+QP2+QP3+QP4
            if NQ<0.0:                              
                temp = pH
                pH = pH-((pH-pHprev)/2.0)
                pHnext = temp
            else:
                temp = pH
                pH = pH + ((pHnext-pH)/2.0)
                pHprev = temp

            if (pH-pHprev<E) and (pHnext-pH<E): 
                return pH