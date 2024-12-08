import json
import os

# 하이퍼파라미터 설정
hyperparameters = {
    "latent_dim": 100,
    "num_classes": 10,
    "img_size": 32,
    "batch_size": 64,
    "num_epochs": 100,
    "n_critic": 5,
    "clip_value": 0.01,
    "lr": 0.00005,
    "path": 'weight/GAN_epoch_50.pth'
}

# 하이퍼파라미터를 JSON 파일로 저장하는 함수
def save_hyperparameters_to_json(hyperparameters, receipts_folder='receipts'):
    # receipts 폴더가 없으면 생성
    if not os.path.exists(receipts_folder):
        os.makedirs(receipts_folder)
        print("기본 Hyperparameter Receipt json파일을 생성합니다.")
    
    # 파일명은 하이퍼파라미터에 기반하여 동적으로 생성 (예: 'GAN_latent100_lr0.00005.json')
    filename = f"{receipts_folder}/GAN_latent{hyperparameters['latent_dim']}_lr{hyperparameters['lr']}.json"
    
    # device를 torch.device 객체에서 문자열로 변환하여 저장
    hyperparameters['device'] = str(hyperparameters['device'])  # device는 trainer에서 설정
    
    with open(filename, 'w') as json_file:
        json.dump(hyperparameters, json_file, indent=4)
    
    print(f"하이퍼파라미터가 {filename}에 저장되었습니다.")

# JSON 파일에서 하이퍼파라미터를 불러오는 함수
def load_hyperparameters_from_json(filename):
    with open(filename, 'r') as json_file:
        hyperparameters = json.load(json_file)
    
    # device는 다시 torch.device로 변환
    hyperparameters['device'] = torch.device(hyperparameters['device'])
    
    return hyperparameters

# 하이퍼파라미터 저장 예시
save_hyperparameters_to_json(hyperparameters)

# 저장된 하이퍼파라미터 불러오기 예시
filename = 'receipts/GAN_latent100_lr0.00005.json'
loaded_hyperparameters = load_hyperparameters_from_json(filename)
print("불러온 하이퍼파라미터:", loaded_hyperparameters)
