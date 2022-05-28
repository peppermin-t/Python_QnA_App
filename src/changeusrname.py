import pickle

if __name__ == '__main__':
    original_name = input()
    with open(f'./resource/usrInfos/usr_{original_name}.pkl', 'rb') as f:
        user = pickle.load(f)

    user.name = input()
    with open(f'./resource/usrInfos/usr_{original_name}.pkl', 'wb') as f:
        pickle.dump(user, f)
