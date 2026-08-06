# Model Training Options

## Quick Start

For fastest training (Random Forest + Logistic Regression only):
```bash
python train_models.py --quick
```

## Full Training (All Models)

To train all models including SVM and Neural Networks:
```bash
python train_models.py
```

## Selective Training

### Skip SVM (faster):
```bash
python train_models.py --skip-svm
```

### Skip Neural Network (faster):
```bash
python train_models.py --skip-nn
```

### Skip Both SVM and Neural Network (fastest):
```bash
python train_models.py --skip-svm --skip-nn
```

## Training Time Estimates

- **Quick mode** (RF + LR): ~2-3 minutes
- **With Neural Networks** (RF + LR + NN): ~5-8 minutes  
- **With SVM** (RF + LR + SVM): ~10-15 minutes
- **Full training** (RF + LR + SVM + NN): ~15-25 minutes

## Model Selection in Streamlit Apps

Once models are trained, the Streamlit apps will automatically detect them and add them to the model selection dropdown. The available models will be:

### Telco Churn App:
- Random Forest (best overall)
- Logistic Regression (good balance)
- Neural Network (deep learning)
- SVM (complex boundaries)

### Bank Marketing App:
- Random Forest (best overall)
- Logistic Regression (good balance)
- Neural Network (deep learning)
- SVM (complex boundaries)

## Recommendations

- **For quick demos**: Use `--quick` flag
- **For complete research demonstration**: Use full training (no flags)
- **For limited time**: Use `--skip-svm` (NN is faster than SVM)
- **For maximum model variety**: Train all models without any flags