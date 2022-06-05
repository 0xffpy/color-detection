import numpy as np
import cv2
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle


def k_means_algorithm(cropped_image, num_of_iter=10):
    k_m_image = cropped_image.reshape((-1, 3))
    k_m_image = np.float32(k_m_image)
    param = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, num_of_iter, 1.0)
    k = 1
    ret, label, center = cv2.kmeans(k_m_image, k, None, param, num_of_iter, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    k_means = res.reshape((cropped_image.shape))
    r, g, b = k_means[0, 0].ravel()
    return [int(b), int(g), int(r)]


def clean_data(features, label):
    path = "training_dataset"
    x = os.listdir("training_dataset")
    for i in x:
        path2 = os.path.join(path, i)
        y = os.listdir(path2)
        color = i
        for j in y:
            image = cv2.imread(os.path.join(path2, j))
            rgb_color = k_means_algorithm(image)
            features.append(rgb_color)
            label.append(i)
    # feature, labels = new_data_set()
    # features = features + feature
    # label = label + labels

    X_train, X_test, y_train, y_test = train_test_split(
        features, label, test_size=0.25, shuffle=True)

    return X_train, X_test, y_train, y_test


def train_model(evidence, labels, n_neighbours=13):
    neigh = KNeighborsClassifier(n_neighbors=n_neighbours)
    neigh.fit(evidence, labels)
    return neigh


# now we will try different knn and see which produces the best output from 1 to 15

def main():
    # funny thing is 1 is the best lol
    # the least number of knn ex 1, 3 are the best
    # becase we have limited data set if we increase the number of n we get more values outsied the range which won't work
    # i will show you the visualization.
    # so as you can see the lower the data it may overlap with other color chanel.
    X_train, X_test, y_train, y_test = clean_data([], [])
    # lets do it for 10 times
    max_accuracy = 0
    n_nearest = 0
    flag = False
    for j in range(5):
        for i in range(1, 15, 2):
            X_train, X_test, y_train, y_test = clean_data([], [])
            model = train_model(X_train, y_train, i)
            y_pred = model.predict(X_test)
            print(model.predict(np.array([175.3985, 184.82477, 194.14993]).reshape(-1, 3)))
            accuracy = accuracy_score(y_test, y_pred)
            print(accuracy * 100, "n =", i)
            print(X_test)
            print(y_test)
            if (accuracy * 100) > 95 and accuracy > max_accuracy:
                knnPickle = open("../../../PycharmProjects/pythonProject7/knn_file", 'wb')
                pickle.dump(model, knnPickle)
                print(i)
                print("The accuracy is chosen", accuracy)
                n_nearest = i
                max_accuracy = accuracy
                break

        print(n_nearest, " Is the n")
        print("The accuracy is", max_accuracy)


if __name__ == "__main__":
    print("F".isalnum())
    #main()
