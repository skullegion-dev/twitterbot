# -*- coding: utf-8 -*-
import tweepy
import random
import time
import os
from collections import deque

# Twitter API credentials (hardcoded for testing; replace with your keys)
API_KEY = "652Pj9urb9fBEKDK2dnqIiBpJ"
API_SECRET = "WBcCaoFIK7S909Nes6I0qIWlULreEPd6qKOCtp1Rle5qkjAr8g"
ACCESS_TOKEN = "1900540762057764864-LrWqvdaLux0Yfr4vxzxfRWekQm45ts"
ACCESS_TOKEN_SECRET = "GKT53ZyXzPwoEbaUjfMpZeUqBt4eeb3LPFvDmLW6cjhft"

# Authenticate with v2 API
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Existing keywords (~80+)
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

# Static trending hashtags (fallback)
trending_hashtags = [
    "#MemeCoinSZN", "#SolanaSummer", "#RaydiumRocks", "#DegenSZN", "#CryptoMoon",
    "#BullRun2025", "#AltcoinSeason", "#Web3Vibes", "#NFTs", "#CryptoGems"
]

# Existing dynamic comment components
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

# Fetch real-time crypto/memecoin trends and assess dominance
def fetch_crypto_trends(used_trends):
    try:
        # Get trends for worldwide (WOEID 1)
        trends_response = client.get_place_trends(id=1)
        trends = trends_response.data[0]["trends"]
        # Filter for crypto/memecoin relevance
        crypto_keywords = ["crypto", "memecoin", "coin", "token", "solana", "doge", "shib", "pepe", "pump", "moon", "hodl", "fomo", "btc", "eth"]
        crypto_trends = [trend["name"] for trend in trends if any(kw in trend["name"].lower() for kw in crypto_keywords)]
        
        # Exclude recently used trends
        available_trends = [trend for trend in crypto_trends if trend not in used_trends]
        
        # Calculate crypto dominance (proportion of trends that are crypto-related)
        total_trends = len(trends)
        crypto_count = len(crypto_trends)
        dominance = crypto_count / total_trends if total_trends > 0 else 0
        
        if not available_trends:
            # Fallback to hashtags if no new trends available
            available_trends = [h for h in trending_hashtags if h not in used_trends]
            if not available_trends:
                used_trends.clear()  # Reset if all options exhausted
                available_trends = trending_hashtags
        
        return available_trends, dominance
    except Exception as e:
        print(f"Failed to fetch trends: {e}")
        available_trends = [h for h in trending_hashtags if h not in used_trends]
        if not available_trends:
            used_trends.clear()
            available_trends = trending_hashtags
        return available_trends, 0  # Assume no dominance on failure

# Generate bait tweet
def generate_bait_tweet(keyword, hashtag):
    bait_texts = [
        f"{hashtag} {keyword} going wild—who’s in?",
        f"{hashtag} {keyword} season is here!",
        f"{hashtag} {keyword} vibes—let’s go!",
        f"{hashtag} {keyword} to the moon?",
        f"{hashtag} {keyword} pumping hard!"
    ]
    tweet = random.choice(bait_texts)
    if len(tweet) > 280:
        tweet = tweet[:277] + "..."
    return tweet

# Generate trending topic tweet
def generate_trending_tweet(trend):
    phrases = [
        f"{trend} is buzzing—thoughts?",
        f"{trend} taking over—bullish or bearish?",
        f"Hearing {trend} everywhere—who’s riding this?",
        f"{trend} spiking—next big thing?",
        f"{trend} vibes—crypto fam, you in?"
    ]
    tweet = random.choice(phrases)
    hashtag = random.choice(trending_hashtags)
    emoji = random.choice(emojis)
    full_tweet = f"{tweet} {hashtag} {emoji}"
    if len(full_tweet) > 280:
        full_tweet = full_tweet[:277] + "..."
    return full_tweet

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

# Main bot loop
def run_bot():
    print("Twitter bot started... Posting real-time trends and bait tweets (v2 only)")
    try:
        user = client.get_me()
        username = user.data.username
        print(f"Bot username: @{username}")
    except Exception as e:
        print(f"Failed to verify credentials: {e}")
        return
    
    # Track used trends with a deque (max 20 to avoid repetition)
    used_trends = deque(maxlen=20)
    base_trending_prob = 0.6  # Base probability for trending tweets
    
    while True:
        # Fetch trends and assess crypto dominance
        available_trends, crypto_dominance = fetch_crypto_trends(used_trends)
        
        # Adjust trending tweet probability based on dominance
        # If dominance > 0.3 (30% of trends are crypto), scale probability up to 0.9
        trending_prob = min(base_trending_prob + (crypto_dominance - 0.3) * 2, 0.9) if crypto_dominance > 0.3 else base_trending_prob
        print(f"Crypto dominance: {crypto_dominance:.2f}, Trending prob: {trending_prob:.2f}")
        
        # Decide action based on adjusted probability
        if random.random() < trending_prob and available_trends:
            # Post trending topic tweet
            trend = random.choice(available_trends)
            trending_tweet = generate_trending_tweet(trend)
            try:
                response = client.create_tweet(text=trending_tweet)
                tweet_id = response.data["id"]
                used_trends.append(trend)  # Track used trend
                print(f"Trending tweet posted: {trending_tweet} (ID: {tweet_id})")
            except Exception as e:
                print(f"Failed to post trending tweet for {trend}: {e}")
                time.sleep(60)
                continue
        else:
            # Post bait tweet
            keyword = random.choice(keywords)
            hashtag = random.choice(trending_hashtags)
            bait_tweet = generate_bait_tweet(keyword, hashtag)
            try:
                bait_response = client.create_tweet(text=bait_tweet)
                bait_tweet_id = bait_response.data["id"]
                print(f"Bait tweet posted: {bait_tweet} (ID: {bait_tweet_id})")
            except Exception as e:
                print(f"Failed to post bait tweet for {keyword}: {e}")
                time.sleep(60)
                continue
            
            # Reply to bait tweet
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
        
        # Delay: 30-60 min (~36 posts/day)
        delay = random.randint(1800, 3600)
        print(f"Waiting {delay//60} mins...")
        time.sleep(delay)

if __name__ == "__main__":
    run_bot()