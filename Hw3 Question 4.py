# %%
from random import random

# %%
def hospital_a(iterations):
    days = 0  # Count of days where boys are >= 60%

    for n in range(iterations):
        boy = 0

        for i in range(15):
            if random() >= 0.5:
                boy += 1

        if boy >= 9:
            days += 1

    return days


avg = []
for x in range(100):
    avg.append(hospital_a(1000))

print(
    f"The average number of days where boys are >=60% of births in hospital A is {round(sum(avg)/100)}"
)

# %%
def hospital_b(iterations):
    days = 0  # Count of days where boys are >= 60%

    for n in range(iterations):
        boy = 0

        for i in range(45):
            if random() >= 0.5:
                boy += 1

        if boy >= 27:
            days += 1

    return days


avg = []
for x in range(100):
    avg.append(hospital_b(1000))

print(
    f"The average number of days where boys are >=60% of births in hospital B is {round(sum(avg)/100)}"
)

# %% [markdown]
# Hospital A has more days with at least 60% boys, with an average of around 300 days out of 1000. While hospital B averages at around 115-118 out of 1000 days.
#
# My guess is that the result will be even lower for hospital C because more boys have to be born per day in order to reach 60%.

# %%
def hospital_c(iterations):
    days = 0  # Count of days where boys are >= 60%

    for n in range(iterations):
        boy = 0

        for i in range(100):
            if random() >= 0.5:
                boy += 1

        if boy >= 60:
            days += 1

    return days


avg = []
for x in range(100):
    avg.append(hospital_c(1000))

print(
    f"The average number of days where boys are >=60% of births in hospital C is {round(sum(avg)/100)}"
)

# %% [markdown]
# This confirms my hypothesis as hospital C has even less days with >=60% boys born than hospital B by a factor of almost 5.
