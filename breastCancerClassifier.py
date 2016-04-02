TRAINING_FILE = 'breast_cancer_training.txt'
TESTING_FILE = 'breast_cancer_testing.txt'

def main():

    print("Reading training data...")
    training_set_list = make_training_set(TRAINING_FILE)
    print("Done reading training data\n")

    print("Training classifier...")
    classifier_list = train_classifier(training_set_list)
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_set_list = make_test_set(TESTING_FILE)
    print("Done reading test data \n")

    print("Classifiying records...")
    result_list = classify_test_set(test_set_list, classifier_list)
    print("Done classifying\n")

    report_results(result_list)

    print("Program finished.")


def make_training_set(training_file):
    return []


def train_classifier(training_set):
    return[]


def make_test_set(testing_file):
    return []


def classify_test_set(test_set_list, classifier_list):
    return[]


def report_results(result_list):
    print("Results reported.")