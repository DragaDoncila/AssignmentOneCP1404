TRAINING_FILE = 'breast-cancer-training.txt'
TESTING_FILE = 'breast_cancer_testing.txt'


def main():
    print("Reading training data...")
    training_set_list = make_data_set(TRAINING_FILE)
    # print(training_set_list)
    print("Done reading training data\n")

    print("Training classifier...")
    classifier_list = train_classifier(training_set_list)
    # for element in classifier_list:
    #     print("{:.3f}".format(element))
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_set_list = make_data_set(TESTING_FILE)
    print("Done reading test data \n")

    print("Classifying records...")
    result_list = classify_test_set(test_set_list, classifier_list)
    for element in result_list:
        print(element)
    print("Done classifying\n")

    report_results(result_list)

    print("Program finished.")


def make_data_set(file_name):
    training_file = open(file_name, 'r')
    training_set = []
    for line in training_file:
        # parse through and split at the comma with multiple assignment instead of a list
        patient_id, a1, a2, a3, a4, a5, a6, a7, a8, a9, diagnosis = line.strip().split(',')
        # create a tuple for the patient with the 11 elements, id and diag. first
        if diagnosis == '2':
            new_diag = 'b'
        else:
            new_diag = 'm'
        patient_info = patient_id, new_diag, int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), int(
            a8), int(a9)
        training_set.append(patient_info)
    return training_set


def train_classifier(training_set):
    benign_count = 0
    benign_sum = [0] * 9
    malignant_count = 0
    malignant_sum = [0] * 9

    for patient in training_set:
        if patient[1] == 'b':
            attribute_list = patient[2:]
            benign_sum = sum_lists(benign_sum, attribute_list)
            benign_count += 1
        else:
            attribute_list = patient[2:]
            malignant_sum = sum_lists(malignant_sum, attribute_list)
            malignant_count += 1

    # create benign_averages by each element of benign_sum/benign_count
    # create malignant averages by each element of malignant_sum/malignant_count
    benign_averages = make_averages(benign_sum, benign_count)
    malignant_averages = make_averages(malignant_sum, malignant_count)
    # create classifier_list by (each element benign_averages + each element malignant_averages)/2

    classifier_list = make_averages(sum_lists(benign_averages, malignant_averages), 2)
    return classifier_list


def classify_test_set(test_set_list, classifier_list):
    result_list = []
    # for each patient in the test set
    for patient in test_set_list:
        count_benign = 0
        count_malignant = 0
        # for each attribute of the patient
        for index in range(9):
            # if attribute is greater than corresponding attribute in classifier_list
            if patient[index + 2] >= classifier_list[index]:
                # increase count of malignant attributes
                count_malignant += 1
                #           otherwise
            else:
                # increase count of benign attributes
                count_benign += 1
                #   create result tuple as patient id, benign count, malignant count, diagnosis
        patient_result = patient[0], count_benign, count_malignant, patient[1]
        #   append result tuple to list of result tuples
        result_list.append(patient_result)
    # return result tuple list
    return result_list


def report_results(result_list):
    total_count = 0
    inaccurate_count = 0
    for result_tuple in result_list:
        benign_count, malignant_count, actual_diagnosis = result_tuple[1:]
        total_count += 1
        if benign_count > malignant_count and actual_diagnosis == 'm':
            inaccurate_count += 1
        elif malignant_count > benign_count and actual_diagnosis == 'b':
            inaccurate_count += 1
    print("Of {} patients, there were {} inaccurate diagnoses based on our classifier".format(
        total_count, inaccurate_count))
    print("Results reported.")


def sum_lists(list1, list2):
    sums_list = []
    for index in range(9):
        sums_list.append(list1[index] + list2[index])
    return sums_list


def make_averages(sum_list, count):
    averages = []
    for value in sum_list:
        averages.append(value / count)
    return averages


main()
