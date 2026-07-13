"""Day 2 exercises for practicing Python functions."""

def calcualte_dataset_split(
        total_sampels: int,
        training_percent: float= 70,
        validation_percent:float = 15,
) ->tuple[int,int,int]:
    """Calculate training, validation, and testing dataset sizes."""
    if total_sampels<= 0:
        return 0,0,0

    if training_percent<0 or validation_percent <0:
        return 0,0,0
    
    if training_percent + validation_percent > 100:
        return 0,0,0
    
    training_samples: int = int(total_sampels * training_percent / 100)
    validation_samples: int = int(total_sampels * validation_percent / 100)

    testing_samples: int = int(total_sampels - (training_samples - validation_samples))

    return(training_samples,validation_samples,testing_samples)


print("--- Dataset Split Calculator ---")

dataset_size: int = int(input("Enter the total number of samples: "))

train_percent: float = float(input("Enter the training percentage: "))
val_percent: float = float(input("Enter the validation percentage: "))

train_size, val_size, test_size = calcualte_dataset_split(
    total_sampels=dataset_size,
      training_percent=train_percent,
      validation_percent=val_percent,
      )

if train_size == 0 and val_size == 0 and test_size == 0:
    print("Invalid dataset or percentage.")
else:
    print("\n--- Dataset Split ---")
    print(f"Training samples: {train_size}")
    print(f"Validation samples: {val_size}")
    print(f"Testing samples: {test_size}")


# Exercise 2: Model Accuracy Calculator

def calculate_accuracy(correct_predictions: int,
                       total_predictions: int,
                       ) -> float:
    if total_predictions <= 0 :
        return 0.0
    if correct_predictions < 0:
        return 0.0
    if correct_predictions > total_predictions:
        return 0.0
    
    accuracy: float = correct_predictions / total_predictions * 100
    return accuracy

correct: int = int(input("Enter the number of correct predicitons: "))
total: int = int(input("Enter the number of total predicitons: "))

if correct > total or correct <0 or total <= 0:
    print("Invalid prediction values.")
else:
    model_accuracy : float = calculate_accuracy(total_predictions=total,correct_predictions=correct)
    print(f"Model accuracy: {model_accuracy:.2f}%")

    if model_accuracy >=90 :
        print("Performance level: Excellent")
    elif model_accuracy >=75:
        print("Performance level: Good")
    elif model_accuracy >=50:
       print("Performance level: Needs improvement")
    else:
       print("Performance level: Poor")



def estimate_training_time(
        number_of_epochs: int,
        minutes_per_epoch: float,
) -> float:
    if number_of_epochs <=0 or minutes_per_epoch <= 0:
        return 0.0
    
    return number_of_epochs * minutes_per_epoch

epochs: int = int(input("Enter the number of epochs: "))
minutes: float = float(input("Enter the number of minutes per epoch: "))

total_minutes: float = estimate_training_time(
    number_of_epochs=epochs,
      minutes_per_epoch=minutes)
total_hours: float = total_minutes / 60

if epochs <= 0 or minutes <= 0:
    print("Invalid training values.")
else:
    print(f"Estimated training time: {total_minutes:.2f} minutes")
    print(f"Estimated training time: {total_hours:.2f} hours")

    if total_hours < 1:
        print("Training level: Short training session")
    elif total_hours < 5:
        print("Training level: Medium training session")
    else:
        print("Training level: Long training session")


def estimate_dataset_storage(
        number_of_files: int,
        average_file_size_mb: float
) -> float:
    """Calculate the total dataset storage size in megabytes."""
    if number_of_files <= 0 or average_file_size_mb <= 0:
        return 0.0
    return number_of_files * average_file_size_mb

files: int = int(input("Enter the number of files: "))
file_size_mb: float = float(input("Enter the average size of files in MB: "))

total_size_mb:float= estimate_dataset_storage(
    number_of_files=files,
      average_file_size_mb=file_size_mb)
total_size_gb: float = total_size_mb / 1024

if files <= 0 or file_size_mb <= 0:
    print("Invalid dataset values.")
else:
    print(f"Dataset size: {total_size_mb:.2f} MB")
    print(f"Dataset size: {total_size_gb:.2f} GB")
    if total_size_gb < 1:
        print("Dataset level: Small dataset")
    elif total_size_gb < 10:
        print("Dataset level: Medium dataset")
    else:
        print("Dataset level: Large dataset")



def estimate_api_cost(
        input_tokens: int,
        output_tokens: int,
        input_price_per_million: float = 2.50,
        output_price_per_million: float = 10.00,
) -> tuple[float,float,float]:
    """Calculate input, output, and total API usage costs."""
    if input_tokens < 0 or output_tokens < 0:
        return 0.0, 0.0, 0.0

    input_cost :float = input_tokens / 1000000 * input_price_per_million
    output_cost : float = output_tokens / 1000000 * output_price_per_million
    total_cost : float = input_cost + output_cost

    return input_cost, output_cost, total_cost

input_token_count: int = int(input("Enter the amount of input tokens: "))
output_token_count: int = int(input("Enter the amount of output tokens: "))

cost_data : tuple[float,float,float] = estimate_api_cost(
    input_tokens=input_token_count,
    output_tokens=output_token_count
    )

input_cost: float = cost_data[0]
output_cost: float = cost_data[1]
total_cost: float = cost_data[2]

if input_token_count < 0 or output_token_count < 0:
    print("Invalid token values.")
else:
    print(f"Input cost: ${input_cost:.6f}")
    print(f"Output cost: ${output_cost:.6f}")
    print(f"Total API cost: ${total_cost:.6f}")

    if total_cost < 0.01:
        print("Cost level: Low-cost request")
    elif total_cost < 0.10:
        print("Cost level: Moderate-cost request")
    else:
        print("Cost level: High-cost request")