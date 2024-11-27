import requests

# main functions
def get_pricing_data(cloud, service, region):
    """
    Get pricing data for a given service and region.
    Parsing the cloud is required to get the correct URL.

    Args:
        service (str): The service to get pricing data for.
        region (str): The region to get pricing data for.

    Returns:
        dict: The pricing data for the given service and region.
    """

    cloud = cloud.lower()
    if cloud == "aws":
        region = "us-east-1"
        url = f"https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/{service}/current/index.json"
    elif cloud == "azure":
        region = "eastus"
        url = f"https://prices.azure.com/api/retail/prices?$filter=serviceName eq '{service}' and armRegionName eq '{region}'"
    elif cloud == "gcp":
        region = "us-east1"
    else:
        raise ValueError("Invalid cloud provider. Must be AWS, Azure, or GCP.")

    response = requests.get(url)
    data = response.json()
    return data["products"][service]

def main():
    while True:
        cloud = input("Enter the cloud provider (AWS, Azure, or GCP) or 'exit' to quit: ").strip().lower()
        if cloud == 'exit':
            break

        service = input("Enter service name: ").strip()
        region = input("Enter region: ").strip()
        
        try:
            pricing_data = get_pricing_data(cloud, service, region)
            print(pricing_data)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

# execution code
if __name__ == "__main__":
    main()