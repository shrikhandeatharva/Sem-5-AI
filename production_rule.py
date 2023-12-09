# Define a list of production rules for medical diagnosis
diagnosis_rules = [
    {
        'condition': lambda symptoms: 'fever' in symptoms and 'cough' in symptoms,
        'action': lambda: "You might have a respiratory infection."
    },
    {
        'condition': lambda symptoms: 'fever' in symptoms and 'rash' in symptoms,
        'action': lambda: "You might have a viral rash."
    },
    {
        'condition': lambda symptoms: 'headache' in symptoms and 'nausea' in symptoms,
        'action': lambda: "You might have a migraine."
    },
    {
        'condition': lambda symptoms: 'fever' in symptoms and 'chills' in symptoms,
        'action': lambda: "You might have a bacterial infection."
    },
    {
        'condition': lambda symptoms: 'fever' in symptoms,
        'action': lambda: "You have a fever, but the exact cause is unclear."
    },
    {
        'condition': lambda symptoms: True,
        'action': lambda: "Sorry, we couldn't make a diagnosis based on your symptoms."
    }
]

# Define the production system for medical diagnosis
def medical_diagnosis(symptoms):
    for rule in diagnosis_rules:
        if rule['condition'](symptoms):
            return rule['action']()

# Test the medical diagnosis production system
patient_symptoms1 = [  'headache']
patient_symptoms2 = ['fever', 'cough', 'headache']
result1 = medical_diagnosis(patient_symptoms1)
result2 = medical_diagnosis(patient_symptoms2)
print(result1)
print(result2)
