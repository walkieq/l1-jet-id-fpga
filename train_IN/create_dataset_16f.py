import numpy as np
import h5py
import os

#os.system("zenodo_get 10.5281/zenodo.3602260 -o data")
#os.system("tar xvzf data/hls4ml_LHCjet_150p_train.tar.gz -C data/")
#os.system("tar xvzf data/hls4ml_LHCjet_150p_val.tar.gz -C data/")

# Data PATH
TRAIN_PATH = "data/train/"
TEST_PATH = "data/val/"


first = True
for file in os.listdir(TRAIN_PATH):
    print("Appending %s" % file)

    with h5py.File(TRAIN_PATH + file, "r") as data:
        if first:
            first = False
            #jetConstituent = data["jetConstituentList"][:, :, [5, 8, 11]]
            jetConstituent = data["jetConstituentList"][:, :, :]
            target = data["jets"][:, -6:-1]
            print("Keys in H5PY files = ", list(data.keys()))
            print(" ")
            featurenames = data.get("jetFeatureNames")
            print("Jets Features = ", featurenames[:])
            print(" ")
            featurenames = data.get("particleFeatureNames")
            print("Jet Constituents Features = ", featurenames[:])
            print(" ")
            images = data.get("jetImage")
            print("Jet Images = ", images[:])
            print("Jet Image Shape = ", images.shape)
            print(" ")
        else:
            # Read (Pt,Etarel,Phirel)
            jetConstituent = np.concatenate(
                #[jetConstituent, data["jetConstituentList"][:, :, [5, 8, 11]]], axis=0
                [jetConstituent, data["jetConstituentList"][:, :, :]], axis=0
            )
            target = np.concatenate([target, data["jets"][:, -6:-1]], axis=0)

print("Target shape =", target.shape)
print("Jet Constituents shape =", jetConstituent.shape)


first = True
for file in os.listdir(TEST_PATH):
    print("Appending %s" % file)

    with h5py.File(TEST_PATH + file, "r") as data:
        if first:
            first = False
            #jetConstituent = data["jetConstituentList"][:, :, [5, 8, 11]]
            jetConstituent_test = data["jetConstituentList"][:, :, :]
            target_test = data["jets"][:, -6:-1]
            print("Keys in H5PY files = ", list(data.keys()))
            print(" ")
            featurenames = data.get("jetFeatureNames")
            print("Jets Features = ", featurenames[:])
            print(" ")
            featurenames = data.get("particleFeatureNames")
            print("Jet Constituents Features = ", featurenames[:])
            print(" ")
            images = data.get("jetImage")
            print("Jet Images = ", images[:])
            print("Jet Image Shape = ", images.shape)
            print(" ")
        else:
            # Read (Pt,Etarel,Phirel)
            jetConstituent_test = np.concatenate(
                #[jetConstituent, data["jetConstituentList"][:, :, [5, 8, 11]]], axis=0
                [jetConstituent_test, data["jetConstituentList"][:, :, :]], axis=0
            )
            target_test = np.concatenate([target_test, data["jets"][:, -6:-1]], axis=0)

print("Target shape =", target_test.shape)
print("Jet Constituents shape =", jetConstituent_test.shape)



# The dataset is N_jets x N_constituents x N_features
njet = jetConstituent.shape[0]
nconstit = jetConstituent.shape[1]
nfeat = jetConstituent.shape[2]

print ("njet    " , njet    )
print ("nconstit" , nconstit)
print ("nfeat   " , nfeat   )

#exit()

## Filter out constituents with Pt<2GeV
#Ptmin = 2.0
#constituents = np.zeros((njet, nconstit, nfeat), dtype=np.float32)
#ij = 0
max_constit = 150
#for j in range(njet):
#    ic = 0
#    for c in range(nconstit):
#        if jetConstituent[j, c, 0] < Ptmin:
#            continue
#        constituents[ij, ic, :] = jetConstituent[j, c, :]
#        ic += 1
#    if ic > 0:
#        if ic > max_constit:
#            max_constit = ic
#        target[ij, :] = target[j, :]  # assosicate the correct target a given graph
#        ij += 1
#
#
## Resizes the jets constituents and target arrays
jetConstituent = jetConstituent[:, 0:max_constit, :]
jetConstituent_test = jetConstituent_test[:, 0:max_constit, :]

len_val = int(0.1 * len(jetConstituent))
jetConstituent_val = jetConstituent[0:len_val, 0:max_constit, :]
target_val         = target[0:len_val, :]

#target = target[0:ij, :]

# transform pt -> log(pt+1)
# jetConstituent[:, :, 0] = np.log(jetConstituent[:, :, 0] + 1)
np.save("data/jetConstituent_train_150_16f.npy", jetConstituent)
np.save("data/jetConstituent_train_target_150_16f.npy", target)
print("Target train dataset shape =", target.shape)
print("Jet Constituents train dataset shape =", jetConstituent.shape)


#np.save("data/jetConstituent_val_150_16f.npy", jetConstituent_val)
#np.save("data/jetConstituent_val_target_150_16f.npy", target_val)
#print("Target val datatset shape =", target_val.shape)
#print("Jet Constituents val dataaset shape =", jetConstituent_val.shape)


np.save("data/jetConstituent_val_150_16f.npy", jetConstituent_test)
np.save("data/jetConstituent_val_target_150_16f.npy", target_test)
print("Target val datatset shape =", target_test.shape)
print("Jet Constituents val dataaset shape =", jetConstituent_test.shape)

