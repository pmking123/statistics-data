compute DUM1=(FERTIL=1) . 
compute DUM2=(FERTIL=2) .	
execute .	
compute K3=10.7 . 
compute K1=3.4 . 
compute K2=1.1 . 
compute SIGMA=2.3 . 
execute.	
compute NOISE=rv.normal(0,1) . 
compute Y= K3 + K1*DUM1 + K2*DUM2 + SIGMA*NOISE . 
execute.	
glm    Y by FERTIL
  /print parameter    
  /design FERTIL .	
