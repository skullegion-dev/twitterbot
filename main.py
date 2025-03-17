# -*- coding: utf-8 -*-
import tweepy
import random
import time
import os

# Twitter API credentials
API_KEY = os.getenv("652Pj9urb9fBEKDK2dnqIiBpJ")
API_SECRET = os.getenv("WBcCaoFIK7S909Nes6I0qIWlULreEPd6qKOCtp1Rle5qkjAr8g")
ACCESS_TOKEN = os.getenv("1900540762057764864-LrWqvdaLux0Yfr4vxzxfRWekQm45ts")
ACCESS_TOKEN_SECRET = os.getenv("GKT53ZyXzPwoEbaUjfMpZeUqBt4eeb3LPFvDmLW6cjhft")

# Authenticate with v2 API
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Broad keywords (~80+)
keywords = [
    "memecoin", "dogecoin", "shib", "meme crypto", "babydoge", "floki", "pepe coin",
    "doge meme", "shiba inu", "mooncoin", "shitcoin", "crypto meme", "meme token",
    "viral coin", "degen coin", "hype coin", "meme coin pump", "meme coin drop",
    "cheap coin", "fast coin", "meme coin season", "meme coin craze", "token meme",
    "meme coin gem", "rugpull", "pump and dump", "raydium", "solana meme", "sol meme",
    "raydium launch", "solana launch", "solana token", "raydium pool", "solana hype",
    "raydium meme", "solana shitcoin", "solana moon", "raydium token", "solana degen",
    "raydium hype", "solana pump", "pumpfun", "dexscreener", "moondex", "raydium dex",
    "solana dex", "pump token", "crypto pump", "token launch", "moon token", "crypto viral",
    "crypto degen", "bull run meme", "bear market meme", "crypto moon", "to the moon",
    "lambo coin", "diamond hands", "paper hands", "hodl meme", "fomo coin", "fud coin",
    "catcoin", "eloncoin", "safemoon", "bonk coin", "wen coin", "meme lord", "doge killer",
    "shib army", "pepe army", "floki inu", "crypto trend", "meme coin news", "viral crypto",
    "hot coin", "next doge", "meme coin 2025", "crypto gem", "low cap coin", "microcap meme",
    "hidden gem coin"
]

# Trending hashtags (update weekly from x.com/explore)
trending_hashtags = [
    "#MemeCoinSZN", "#SolanaSummer", "#RaydiumRocks", "#DegenSZN", "#CryptoMoon"
]

# Trending crypto/memecoin topics (update periodically from x.com/explore or news)
trending_topics = [
    "Bitcoin hitting 100k soon? #BTC", "Ethereum ETF hype is real #ETH",
    "Solana memecoins taking over #SOL", "Raydium pumps new tokens #Raydium",
    "Dogecoin moon rumors again #DOGE", "Shiba Inu burns heating up #SHIB",
    "Pepe coin flipping the charts #PEPE", "Floki Inu Elon tweet boost #FLOKI",
    "Bonk coin Solana’s new star #BONK", "Wen moon for memecoins? #Wen",
    "Pump.fun launches go wild #PumpFun", "Degen trading season is back #Degen",
    "Microcap gems popping off #LowCap", "Safemoon v2 revival? #Safemoon",
    "Catcoin claws its way up #Catcoin"
]

# Dynamic comment components (for bait-and-reply)
intros = [
    "Yo, just 0.05 SOL", "Only 0.05 SOL", "For a tiny 0.05 SOL", "Drop 0.05 SOL",
    "With a mere 0.05 SOL", "At dirt-cheap 0.05 SOL", "0.05 SOL is all you need",
    "Steal this: 0.05 SOL", "Low-key 0.05 SOL", "Bargain 0.05 SOL"
]
actions = [
    "to launch", "to create", "to drop", "to build", "to whip up", "to crank out",
    "to spin up", "to fire off", "to pump out", "to unleash", "to craft", "to blast"
]
descriptors = [
    "a Raydium memecoin", "a viral Raydium coin", "your meme banger", "a Solana hit",
    "a cheap Raydium gem", "a quick meme token", "a hype coin", "a memecoin beast",
    "a Raydium rocket", "a Solana moonshot", "a meme king", "a viral sensation"
]
hype_phrases = [
    "Dirt cheap!", "Stupid easy!", "Too good!", "Insane value!", "Lightning fast!",
    "Cheaper than coffee!", "Easiest ever!", "Unreal deal!", "Mind-blowing!",
    "Game-changer!", "No-brainer!", "Pure fire!", "Next-level!", "Can’t beat it!"
]
calls_to_action = [
    "Hit memecoinscreator.fun NOW", "Check memecoinscreator.fun",
    "Jump on memecoinscreator.fun", "Go to memecoinscreator.fun",
    "Try memecoinscreator.fun ASAP", "Visit memecoinscreator.fun",
    "Get in at memecoinscreator.fun", "Launch at memecoinscreator.fun",
    "Score it at memecoinscreator.fun", "Grab it on memecoinscreator.fun"
]
emojis = [
    "🚀", "🔥", "💰", "🌙", "💎", "🎉", "⚡", "📈", "🌟", "🤑", "✨", "👑", "🎯", "💪"
]
boosters = [
    "in 2 mins", "with 1 click", "no sweat", "like magic", "in a snap", "so quick",
    "effortless", "right now", "instantly", "boom"
]

# Generate bait tweet
def generate_bait_tweet(keyword, hashtag):
    bait_texts = [
        f"{hashtag} {keyword} going wild—who’s in?",
        f"{hashtag} {keyword} season is here!",
        f"{hashtag} {keyword} vibes—let’s go!",
        f"{hashtag} {keyword} to the moon?",
        f"{hashtag} {keyword} pumping hard!"
    ]
    return random.choice(bait_texts)

# Generate unique reply comment
def generate_unique_comment():
    intro = random.choice(intros)
    action = random.choice(actions)
    descriptor = random.choice(descriptors)
    hype = random.choice(hype_phrases)
    cta = random.choice(calls_to_action)
    emoji = random.choice(emojis)
    booster = random.choice(boosters)
    return f"{intro} {action} {descriptor}? {hype} {cta} {booster} {emoji}"

# Generate trending topic tweet
def generate_trending_tweet():
    topic = random.choice(trending_topics)
    if len(topic) > 280:
        topic = topic[:277] + "..."
    return topic

# Main bot loop (mix bait-and-reply with trending topic posts)
def run_bot():
    print("Twitter bot started... Mixing bait tweets, replies, and trending topics (v2)")
    try:
        user = client.get_me()
        username = user.data.username
        print(f"Bot username: @{username}")
    except Exception as e:
        print(f"Failed to verify credentials: {e}")
        return
    
    while True:
        # Randomly choose: 50% bait-and-reply, 50% trending topic
        if random.random() < 0.5:  # 50% chance for bait-and-reply
            keyword = random.choice(keywords)
            hashtag = random.choice(trending_hashtags)
            
            # Step 1: Post bait tweet
            bait_tweet = generate_bait_tweet(keyword, hashtag)
            if len(bait_tweet) > 280:
                bait_tweet = bait_tweet[:277] + "..."
            try:
                bait_response = client.create_tweet(text=bait_tweet)
                bait_tweet_id = bait_response.data["id"]
                print(f"Bait tweet posted: {bait_tweet} (ID: {bait_tweet_id})")
            except Exception as e:
                print(f"Failed to post bait tweet for {keyword}: {e}")
                time.sleep(60)  # Wait 1 min and retry
                continue
            
            # Step 2: Reply to bait tweet
            comment = generate_unique_comment()
            reply_text = f"@{username} {comment}"
            if len(reply_text) > 280:
                reply_text = reply_text[:277] + "..."
            try:
                reply_response = client.create_tweet(
                    text=reply_text,
                    in_reply_to_tweet_id=bait_tweet_id
                )
                print(f"Replied to {bait_tweet_id}: {reply_text}")
            except Exception as e:
                print(f"Failed to reply for {keyword}: {e}")
            
            print("Posted bait-and-reply pair")
        
        else:  # 50% chance for trending topic tweet
            trending_tweet = generate_trending_tweet()
            try:
                trending_response = client.create_tweet(text=trending_tweet)
                print(f"Trending topic posted: {trending_tweet} (ID: {trending_response.data['id']})")
            except Exception as e:
                print(f"Failed to post trending tweet: {e}")
                time.sleep(60)  # Wait 1 min and retry
                continue
        
        # Delay to average ~48 posts/day (1,440/month)
        delay = random.randint(2400, 3000)  # 40-50 min
        print(f"Waiting {delay//60} mins...")
        time.sleep(delay)

if __name__ == "__main__":
    run_bot()