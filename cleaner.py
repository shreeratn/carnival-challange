# %%
import pandas as pd

# %%
fname = input("Enter file name with extension\n\n").strip()
train = pd.read_csv(fname)

# %%
train.drop(["Product_id", "instock_date", "Customer_name"], axis=1, inplace=True)

# %%
train["Stall_no"].fillna(51, inplace=True)
train["Stall_no"] = train["Stall_no"].astype(int)

# %%
train["Loyalty_customer"] = train["Loyalty_customer"].map({"Yes": 1, "No ": 0})

# %%
cat_name = train["Product_Category"].unique()
cat_index = [i for i in range(len(cat_name))]
cat_dc = dict(zip(cat_name, cat_index))
# print(cat_dc)
train["Product_Category"] = train["Product_Category"].map(cat_dc)

# %%
train["Discount_avail"].interpolate(method="nearest", inplace=True)
train["Discount_avail"] = train["Discount_avail"].astype(int)

# %%
train["charges_1"].interpolate(method="linear", inplace=True)
train["charges_1"] = train["charges_1"].astype(int)

# %%
train["charges_2 (%)"].interpolate(method="slinear", inplace=True)
train["charges_2 (%)"] = train["charges_2 (%)"].astype(int)

# %%
train["Minimum_price"].interpolate(method="linear", inplace=True)

# %%
train["Maximum_price"].interpolate(method="linear", inplace=True)

# %%
train["Selling_Price"].interpolate(method="linear", inplace=True)

# %%
print("\n\nFile saved as ................   " + ('clean'+fname))
train.to_csv(('clean_'+fname), index=False)

for i in range(300):
    continue

print("Now Exiting")
