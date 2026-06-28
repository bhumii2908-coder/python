# collecting user feedback
feetback=["great service","very good","could be better","excellent","averge"]

# adding new feedback
feetback.append("not happy")

# counting specific feedback
positive_feetback_count= sum(1 for comment in feetback if "great" in comment.lower() or "excellent" in comment.lower()) 
print(f"positive feetback count:{positive_feetback_count}")


# printing all feedback
print("user feetback:")
for comment in feetback:
    print(f"- {comment}")
