import pandas as pd

MODEL_VERSION = "1.0.0"


def predict_output(model, label_encoder, input_data: dict) -> dict:
    """
    Runs inference on a single input record.
    """

    df = pd.DataFrame([input_data])

    predicted_class_num = model.predict(df)[0]

    predicted_class = label_encoder.inverse_transform(
        [predicted_class_num]
    )[0]

    probs = model.predict_proba(df)[0]

    class_probs = {
        label_encoder.inverse_transform([cls])[0]: float(round(prob, 4))
        for cls, prob in zip(model.classes_, probs)
    }

    confidence = float(round(class_probs[predicted_class], 4))

    return {
        "predicted_category": str(predicted_class),
        "confidence": confidence,
        "class_probabilities": class_probs,
        "model_version": MODEL_VERSION
    }
