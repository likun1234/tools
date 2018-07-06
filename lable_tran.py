    import numpy as np  
    import glob  
    import os  
    import random  
      
    def main():  
        train_dir = "./image/"  
        test_dir = "./image/"  
        train_path = "./train.txt"  
        test_path = "./test.txt"  
        train_images = glob.glob(os.path.join(train_dir, "*.jpg"))  
        test_images = glob.glob(os.path.join(test_dir, "*.jpg"))  
        train_file = open(train_path, 'a')  
        test_file = open(test_path, 'a')  
        print(len(train_images))  
        print(len(test_images))  
        for idx in range(len(train_images)):  
            train_name, _ = os.path.splitext(os.path.basename(train_images[idx]))  
            train_content = train_name + "\n"  
            train_file.write(train_content)  
        train_file.close()  
        for idx in range(len(test_images)):  
            test_name, _ = os.path.splitext(os.path.basename(test_images[idx]))  
            test_content = test_name + "\n"  
            test_file.write(test_content)  
        test_file.close()  
      
    if __name__ == '__main__':  
        main()  
