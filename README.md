# Wrap Up Report

**팀명**: Happyface

|[남세현](https://github.com/ntommy11)|[김연주](https://github.com/kimyeondu)|[김준홍](https://github.com/JoonHong-Kim)|[김현수](https://github.com/shawnhyeonsoo)|[안영진](https://github.com/snoop2head)|[전재영](https://github.com/hihellohowareyou)|[최성욱](https://github.com/jjonhwa)|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/ntommy11)|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/kimyeondu)|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/JoonHong-Kim)|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/shawnhyeonsoo)|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/snoop2head)|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/hihellohowareyou)|[![Untitled](https://user-images.githubusercontent.com/30318926/142752785-e6f354d8-7654-42fa-b42a-a89fefcf196b.png)](https://github.com/jjonhwa)|


dataset은 data/re.csv 파일을 이용하면 됩니다. 
데이터의 비율은 다음과 같습니다.

![image](https://user-images.githubusercontent.com/87692784/142753360-d659fe9b-72a7-4337-a9fb-79c4cabd942e.png)




### 1차 가이드라인 및 relation 설정

위키문서들을 살펴보고 문서내 분포와 it기업이라는 주제에 맞는 relation 12개를 설정했다. relation의 분포데이터의 분포를 따르되 no relation의 경우에는 전체의 50%를 할당하기로 하고 다른 relation에 대한 태깅이 끝난 후 진행하기로 했다. 

- [1차 Relation Set](https://docs.google.com/spreadsheets/d/1Oe4dejSKRmDRLgY6ie6KXXqjOZ6LhIz-vt6tUgJoivk/edit#gid=0)
- [1차 Guideline](https://docs.google.com/document/d/1oaSh0cxbrqIAPlS_bkzaFi7RFQiiD5f-/edit)

### 데이터 전처리

- 팀은 가이드라인 작성에 앞서서, 먼저 문서를 문장 단위로 나누는 작업을 진행했다.
- 문서를 문장으로 나누는 것은 kss 모듈을 이용하여 진행했으며, kss의 pynori tokenizer을 갖고 문장들을 나눈 결과 2505 문장이 도출되었다.
- 해당 문장들을 tagtog에 업로드하면서 협업을 시작했다.

### 파일럿 태깅

- Tagtog에서 파일을 추출한 뒤에 google spreadsheet에 업로드 하는 작업을 진행했다.
- 한 사람당 10개의 예시를 가지고 pilot tagging을 통해 애매했던 부분에 대하여 좀더 명확한 기준을 세웠다.
- 새로운 기준을 바탕으로 가이드라인과 관계를 업데이트 하였다.
    - [2차 Relation Set](https://docs.google.com/spreadsheets/d/1SK54BaWppFaM_7jG3bQBan4AhrU7U_P5Ao2vs2i6t9w/edit#gid=0)
    - [2차 Guideline](https://docs.google.com/document/d/198zmOBEr5fVNm4-3_FXOkKFs3FHUSmzi/edit?rtpof=true)

### 파이럿 태깅 후 Relation 및 가이드라인 수정

- 파일럿 태깅 후 분포가 너무 적거나 의미가 애매한 라벨은 제거하였다.
- 다른 라벨과 의미가 겹치는'**단체:상위_단체','단체:자회사','단체:모회사'** 3개의 라벨을 제거하고, '**단체:하위_단체**'에 포함하였다.
- 회사가 만든 제품의 **기능** 같은 경우에는 대명사로 표현이 될 시 '**단체: 제품**' 에 포함시키기로 하였다.
- 추가로 기업들간의 관계로 계약관계('**단체:계약_단체**')를 추가해서 총 10개의 relation을 설정했다. 이때 기업의 지분 계약(투자, M&A 등)이 아닌 서비스와 재화 제공의 계약 관계로 한정하여서 relation을 설정하였다.
- **'No_Relation'** 의 경우, 발견한 관계와 비율을 1:1로 설정해 Tagging을 진행했다.

### 태깅 및 Relation 데이터 교차 검수

- 각자 약 360개의 데이터 tagging 진행
- 각자에게서 28개의 데이터를 random sampling하여 교차 검수했으며, 개인 당 168개의 라벨들을 라벨링했다.

### Relation 평가

![Untitled 1](https://user-images.githubusercontent.com/30318926/142752801-8846a35c-d332-4835-9f94-033a4578a95a.png)

- Fleiss' Kappa는 0.887이 나왔다.
- 80% 20%의 비율로 train,valid 데이터셋을 나눠 학습해보내 klue/roberta-large 기준 f1 score 71점을 기록했습니다.
- 데이터가 많진 않았지만 데이터간의 관계가 명확하고 너무 쉽거나 어렵지 않은 데이터셋이라는 내부평가를 내렸다.

### 의의

- 각자의 인지적 차이가 있었기 때문에, 명확한 기준을 세우기까지에 많은 논의가 필요했다.
- 데이터셋을 직접 제작해보면서 고품질의 데이터가 얼마나 귀한지에 대한 소중함을 깨달았다.
- 데이터셋을 구축하는 일반적인 프로세스를 학습하였다.
- Knowledge Graph구축을 위한 IT기업에 대한 정보를 담은 relation으로 사용할 것으로 기대한다. 특히 대부분의 Relation은 TACRED의 relation을 따르고 있어 TACRED의 relation과 함께 사용할 수 있을것이다. 또한 기업에 특화된 relation인 계약관계를 추가하여 IT기업에 대한 정보와 IT기업간의 관계를 자세히 담아낼 수 있을 것이다.
