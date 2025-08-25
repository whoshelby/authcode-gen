import base64, hashlib, hmac, struct, time, sys

def decode(secret):
    secret = secret.replace(" ", "").upper()
    secret += "=" * ((-len(secret)) % 8)
    return base64.b32decode(secret, casefold=True)

def hotp(key, counter, digits=6, algo="sha1"):
    h = hmac.new(key, struct.pack(">Q", counter), getattr(hashlib, algo)).digest()
    o = h[-1] & 15
    num = (h[o] & 127) << 24 | (h[o+1] & 255) << 16 | (h[o+2] & 255) << 8 | (h[o+3] & 255)
    return str(num % (10 ** digits)).zfill(digits)

def totp(secret, step=30, digits=6, algo="sha1"):
    now = int(time.time())
    return hotp(decode(secret), now // step, digits, algo), step - (now % step)

def main():
    secret = input("Enter Base32 secret: ").strip()
    if not secret:
        print("Secret cannot be empty")
        return

    try:
        decode(secret) 
        print("[*] Generating codes... (Ctrl+C to quit)\n")
        while True:
            code, left = totp(secret)
            sys.stdout.write(f"\r{code}   {left:2d}s left")
            sys.stdout.flush()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped")

if __name__ == "__main__":
    main()
