import argparse
from bot import place_order

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

# Normalize input
args.side = args.side.upper()
args.type = args.type.upper()

# Validation
if args.side not in ["BUY", "SELL"]:
    print("Invalid side. Use BUY or SELL")
    exit()

if args.type not in ["MARKET", "LIMIT"]:
    print("Invalid type. Use MARKET or LIMIT")
    exit()

if args.type == "LIMIT" and not args.price:
    print("LIMIT order requires price")
    exit()

res = place_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

print("\n=== ORDER SUMMARY ===")
print(f"Symbol: {args.symbol}")
print(f"Side: {args.side}")
print(f"Type: {args.type}")
print(f"Quantity: {args.quantity}")
if args.price:
    print(f"Price: {args.price}")

print("\n=== RESPONSE ===")

if "error" in res:
    print(f"❌ Failed: {res['error']}")
else:
    print(f"Order ID: {res.get('orderId')}")
    print(f"Status: {res.get('status')}")
    print(f"Executed Qty: {res.get('executedQty')}")
    print(f"Avg Price: {res.get('avgPrice')}")