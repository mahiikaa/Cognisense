class MultimodalFatigueModel:
    def __init__(self):
        print("Model initialized!")

    def predict(self, input_data):
        print("Running simulated prediction...")

        face = input_data.get("face", "")
        voice = input_data.get("voice", "")
        behavior = input_data.get("behavior", "")

        result = []

        # Simulated rules for face data
        if "eye_closed" in face or "yawning" in face:
            result.append("fatigued (face)")
        else:
            result.append("not fatigued (face)")

        # Simulated rules for voice data
        if "slow" in voice or "slurred" in voice:
            result.append("fatigued (voice)")
        else:
            result.append("not fatigued (voice)")

        # Simulated rules for behavior data
        if "low typing speed" in behavior or "no mouse movement" in behavior:
            result.append("fatigued (behavior)")
        else:
            result.append("not fatigued (behavior)")

        return result

