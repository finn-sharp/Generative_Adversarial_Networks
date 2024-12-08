# Conditional DCGAN with WGAN Objective

> [!NOTE]
> ## 프로젝트 설명
> 이 프로젝트는 CIFAR-10 데이터셋을 사용하여 이미지를 생성하는 Conditional DCGAN 모델입니다.  
> 다음 세 가지 주요 조건을 충족하도록 설계되었습니다:
> 
> 1. **Conditional GAN (cGAN)**  
>    - 클래스 레이블(조건)을 생성자와 비판자 모델의 입력에 반영하여 특정 클래스에 해당하는 이미지를 생성합니다.
>    
> 2. **Deep Convolutional GAN (DCGAN)**  
>    - 생성자와 비판자 모두 CNN(Convolutional Neural Network)을 활용하여 이미지를 처리합니다.
>    
> 3. **WGAN Objective**  
>    - Wasserstein GAN의 목적 함수와 가중치 클리핑 기법을 적용하여 안정적인 학습을 보장합니다.

---

## 데이터셋
- **CIFAR-10**: 10개의 클래스가 포함된 32x32 크기의 컬러 이미지 데이터셋.
- 본 프로젝트에서는 CIFAR-10의 모든 클래스에 대한 조건부 이미지를 생성합니다.

---

## 주요 파일 및 구조
- **`trainer.ipynb`**: GAN 모델 정의 및 학습 스크립트.
- **`README.md`**: 프로젝트 설명 문서.
- **`data/`**: CIFAR-10 데이터가 다운로드되는 디렉토리.

---

## 설치 및 실행

### 1. 의존성 설치
다음 명령어로 필요한 라이브러리를 설치하세요:
```bash
pip install -r requirements.txt
```
