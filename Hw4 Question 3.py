# You suspect that a new device causes cancer in its users. What data should you see if your suspicion is correct?
# If the device raises the cancer rate of its users by 1%,
# will you clearly see the effect if you survey 1,000 people? How about 10,000 or 100,000?

# %% [markdown]
# If my suspicion is correct, I should see an increase in the amount of people with cancer in the population. <br> <br>
# In order to make the correlation that the device is the cause of cancer, we have to determine the proportion of the population that has this device, along with the proportion of users which got cancer after getting the device.
# If there is a significant enough correlation between the two, then we can determine that there is likely a link between the device and cancer. <br> <br>
# I will create a simulation to test out the hypothesis. <br><br>
# For the purpose of the simulation, let's say that 5% of the population will be diagnosed with cancer. <br><br>
# If we only survey people who own the device, and our suspicion is correct, we should see that 6% of the population would have cancer.

# %%
from random import random

# %%
def survey(population, iterations):

    # List to store the number of people with cancer in each iteration
    data = []

    for n in range(iterations):
        # We start off by calculating the initial amount of people with cancer already
        cancer = population * 0.05

        # Then we calculate the chance of those who don't have cancer to develop cancer after using the device
        for i in range(round(population - cancer)):
            if random() <= 0.01:
                cancer += 1

        # Store the amount of people with cancer
        data.append(cancer)

    # Calculate the average number of people with cancer after all iterations passed
    avg = round(sum(data) / iterations)

    # Return the new amount of cancer patients and the new proportion of the population with cancer
    return avg, round((avg / population) * 100, 2)


# %%

small_survey = survey(1000, 1000)
med_survey = survey(10000, 1000)
big_survey = survey(100000, 1000)

print(
    f"""
After surveying 1,000 people, {small_survey[0]} of them have cancer. Or {small_survey[1]}% of the population.
After surveying 10,000 people, {med_survey[0]} of them have cancer. Or {med_survey[1]}% of the population.
After surveying 100,000 people, {big_survey[0]} of them have cancer. Or {big_survey[1]}% of the population.
      """
)

#%%
# For this function, I will show how a 1% increase of cancer rate in device users affects the total population.
def nsurvey(survey, iterations):
    # I will set the total population to be a fixed number of 1,000,000.
    pop = 10000000
    data = []

    for n in range(iterations):
        cancer = pop * 0.05

        # For each person surveyed that does not have cancer, randomly choose who will get cancer.
        for i in range(round(survey - (survey * 0.05))):
            if random() <= 0.01:
                cancer += 1

        data.append(cancer)

    avg = round(sum(data) / iterations)
    percentage = (avg / pop) * 100

    return avg, round(percentage, 2)


#%%
small = nsurvey(1000, 1000)
med = nsurvey(10000, 1000)
big = nsurvey(100000, 1000)
xtra = nsurvey(1000000, 100)  # 1000 iterations takes too long to calculate.

print(
    f"""
With a total population of 1,000,000 people, {int(1000000 * 0.05)} people should have cancer.
After surveying 1,000 people, the new number of people with cancer becomes {small[0]}. Or {small[1]}% of the population.
After surveying 10,000 people, the new number of people with cancer becomes {med[0]}. Or {med[1]}% of the population.
After surveying 100,000 people, the new number of people with cancer becomes {big[0]}. Or {big[1]}% of the population.
After surveying the whole population, the new number of people with cancer becomes {xtra[0]}. Or {xtra[1]}% of the population.
      """
)

# %%[markdown]
# As you can see from above, the more people we survey, the higher the number of cancer diagnosed. <br> <br>
# This is due to the fact that surveying a small amount of people gives an inaccurate representation of the device's effects. <br> <br>
# I have included a statistic for surveying the entire population so we can see the difference that surveying more people makes. <br> <br>
