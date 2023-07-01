class Codec:
    a = dict()
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    def encode(self, longUrl):
        x = ""
        y = 0
        while y < 7:
            x =x + (random.choice(self.char_set))
            y += 1
        self.a[x] = longUrl
        return x
    def decode(self, shortUrl):
        return self.a[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))