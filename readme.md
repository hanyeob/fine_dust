# 최종목표
> 야외 미세먼지 예측 데이터 + 시간표 => 교내 미세먼지 예측
> ## 현 머신러닝 목표
> > 방대한 데이터(교내 미세먼지측정 데이터)를 라벨링할 수 있는 모델  

# ncs_based

> ## csv files
> > 원본 파일이 있습니다.
> 
> ## ncs_based
> > ### saved_model
> > > nsc_attendModel, nsc_ventModel, nsc_timetableModel,
> > > > 10 features를 기반으로 라벨링 작업후 Tensorflow이용해서 만든 모델입니다.  
> > > > attend: 재실 상황, vent: 환기 상황, timtable: 시간표(최종목표)  
> > ### scaled_data
> > > 원본 데이터를 가공한 데이터입니다. 2_1, 3_1과 같은 숫자 붙은애들은 원본데이터가 잘못된 부분이 있어 사용하지 않고 > 있습니다.  
> > > > MA: moving average(이동평균선), scaled: 정규화  
> > > > attend: 재실 상황, vent: 환기 상황, timtable: 시간표(최종목표)
> > ### *-csv.py
> > > 원본 데이터를 가공하는 파이썬 파일입니다.
> > > > MA: moving average(이동평균선), scaled: 정규화


