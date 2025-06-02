day=int(input(" enter day number :"))
days={ 1: "Monday",
       2: "Tuesday",
       3: "wednesday",
       4: "thursday",
       5: "friday",
       6: "saturday",
       7: "sunday",
}
print(days.get(day,"invalid day number"))
print("Have a nice day")