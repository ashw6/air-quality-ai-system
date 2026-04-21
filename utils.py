def categorize_aqi(aqi):
    if aqi <= 50:
        return 0
    elif aqi <= 100:
        return 1
    elif aqi <= 150:
        return 2
    else:
        return 3


def label(aqi_class):
    return ["Good 😊", "Moderate 😐", "Poor 😷", "Severe ☠️"][aqi_class]