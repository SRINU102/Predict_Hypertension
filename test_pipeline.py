# test_pipeline.py -- simple check that the saved pipeline loads
import joblib, os
pkl = "svm_classifier_pipeline.pkl"   # change filename if your pkl has another name
print("cwd:", os.getcwd())
print("looking for:", pkl)
if not os.path.exists(pkl):
    print("ERROR: file not found:", pkl)
else:
    pipe = joblib.load(pkl)
    print("Pipeline loaded successfully!")
    print(pipe)   # may print long text; it's OK
