#!/usr/bin/env python3
"""
Crypto Casino Affiliate - Backlink Automation Script
Automates social bookmarking and web 2.0 backlink creation
"""

import json
import time
import random
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================
SITE_URL = "https://affiliate99.netlify.app"
SITE_NAME = "StakeReview"
SITE_DESCRIPTION = "Honest crypto casino reviews, guides, and comparisons. Stake Casino, BC.Game, and more."

ARTICLES = [
    {
        "url": f"{SITE_URL}/",
        "title": "Stake Casino Review 2026 — Honest Review, Bonus & Games Guide",
        "description": "Complete Stake Casino review covering 3000+ games, bonuses, payments, and safety. Is Stake legit? We break it all down."
    },
    {
        "url": f"{SITE_URL}/bc-game-review.html",
        "title": "BC.Game Review 2026 — Honest Review, Bonus Code & Games Guide",
        "description": "Complete BC.Game review — up to 180% welcome bonus, daily spin wheel, 2500+ games. Is BC.Game legit? Find out here."
    },
    {
        "url": f"{SITE_URL}/blog/best-crypto-casinos-2026.html",
        "title": "Best Crypto Casinos 2026 — Top 10 Bitcoin Gambling Sites",
        "description": "We compared the top 10 crypto casinos by bonuses, games, withdrawals, and safety. See which crypto casino is #1 in 2026."
    },
    {
        "url": f"{SITE_URL}/blog/stake-vs-bc-game.html",
        "title": "Stake Casino vs BC.Game — Which Is Better in 2026?",
        "description": "Head-to-head comparison of Stake and BC.Game. We compare games, bonuses, payments, user experience, and more."
    },
    {
        "url": f"{SITE_URL}/blog/best-casino-bonuses-2026.html",
        "title": "Best Casino Bonuses 2026 — Top Welcome Offers & Free Spins",
        "description": "The biggest and best casino bonuses in 2026. Welcome offers, no deposit bonuses, free spins compared."
    },
    {
        "url": f"{SITE_URL}/blog/how-to-play-crash-stake.html",
        "title": "How to Play Crash on Stake Casino — Complete Guide 2026",
        "description": "Complete beginner's guide to Stake Crash game. Learn the rules, strategies, and tips to maximize your wins."
    },
    {
        "url": f"{SITE_URL}/blog/best-slots-stake-casino.html",
        "title": "Best Slots on Stake Casino 2026 — Top RTP & Highest Paying Games",
        "description": "Top RTP slots, highest paying games, and new releases at Stake Casino. Find the best slot machines in 2026."
    },
    {
        "url": f"{SITE_URL}/blog/is-stake-casino-legit.html",
        "title": "Is Stake Casino Legit? — Honest Safety Review 2026",
        "description": "Is Stake Casino safe? We examine the license, security, provably fair technology, and real player experiences."
    },
    {
        "url": f"{SITE_URL}/blog/is-bc-game-legit.html",
        "title": "Is BC.Game Legit? — Honest Safety Review 2026",
        "description": "Is BC.Game safe to play at? Complete safety review covering license, security, and player reputation."
    },
    {
        "url": f"{SITE_URL}/blog/how-to-play-stake-casino.html",
        "title": "How to Play at Stake Casino — Complete Beginner's Guide 2026",
        "description": "Step-by-step guide to Stake Casino. Sign up, deposit crypto, claim bonuses, and start playing in minutes."
    },
]

# ============================================================
# SOCIAL BOOKMARKING PLATFORMS
# ============================================================
SOCIAL_BOOKMARKS = [
    {"name": "Reddit", "url": "https://reddit.com/submit", "type": "social"},
    {"name": "Mix", "url": "https://mix.com/submit", "type": "social"},
    {"name": "Flipboard", "url": "https://flipboard.com/submit", "type": "social"},
    {"name": "Pocket", "url": "https://getpocket.com/save", "type": "social"},
    {"name": "Diigo", "url": "https://www.diigo.com/post", "type": "social"},
    {"name": "Folkd", "url": "https://www.folkd.com/submit", "type": "social"},
    {"name": "BibSonomy", "url": "https://www.bibsonomy.org/submit", "type": "social"},
    {"name": "Slashdot", "url": "https://slashdot.org/submit", "type": "social"},
    {"name": "Digg", "url": "https://digg.com/submit", "type": "social"},
    {"name": "Scoop.it", "url": "https://www.scoop.it/submit", "type": "social"},
]

# ============================================================
# WEB 2.0 PLATFORMS
# ============================================================
WEB20_PLATFORMS = [
    {"name": "WordPress.com", "url": "https://wordpress.com", "type": "web20"},
    {"name": "Blogger", "url": "https://www.blogger.com", "type": "web20"},
    {"name": "Tumblr", "url": "https://www.tumblr.com", "type": "web20"},
    {"name": "Medium", "url": "https://medium.com", "type": "web20"},
    {"name": "Weebly", "url": "https://www.weebly.com", "type": "web20"},
    {"name": "Wix", "url": "https://www.wix.com", "type": "web20"},
    {"name": "Jimdo", "url": "https://www.jimdo.com", "type": "web20"},
    {"name": "Webnode", "url": "https://www.webnode.com", "type": "web20"},
    {"name": "Strikingly", "url": "https://www.strikingly.com", "type": "web20"},
    {"name": "Site123", "url": "https://www.site123.com", "type": "web20"},
]

# ============================================================
# CASINO/GAMBLING DIRECTORIES
# ============================================================
DIRECTORIES = [
    {"name": "CasinoMeister", "url": "https://www.casinomeister.com"},
    {"name": "AskGamblers", "url": "https://www.askgamblers.com"},
    {"name": "Casino.org", "url": "https://www.casino.org"},
    {"name": "GamblingSites.com", "url": "https://www.gamblingsites.com"},
    {"name": "OnlineCasino.com", "url": "https://www.onlinecasino.com"},
    {"name": "CasinoListings", "url": "https://www.casinolistings.com"},
    {"name": "Top10", "url": "https://www.top10.com"},
    {"name": "CasinoBonusCenter", "url": "https://www.casinobonuscenter.com"},
    {"name": "iGaming", "url": "https://www.igaming.com"},
    {"name": "BonusFinder", "url": "https://www.bonusfinder.com"},
]

# ============================================================
# FORUMS & COMMUNITIES
# ============================================================
FORUMS = [
    {"name": "Bitcointalk", "url": "https://bitcointalk.org", "niche": "crypto"},
    {"name": "Reddit r/gambling", "url": "https://reddit.com/r/gambling", "niche": "gambling"},
    {"name": "Reddit r/onlinegambling", "url": "https://reddit.com/r/onlinegambling", "niche": "gambling"},
    {"name": "Reddit r/cryptocurrency", "url": "https://reddit.com/r/cryptocurrency", "niche": "crypto"},
    {"name": "CasinoCityTimes", "url": "https://www.casinocitytimes.com", "niche": "casino"},
    {"name": "GamblingForums", "url": "https://www.gamblingforums.co.uk", "niche": "gambling"},
    {"name": "OnlineGambling", "url": "https://www.onlinegambling.com", "niche": "gambling"},
    {"name": "CryptoForum", "url": "https://cryptoforum.com", "niche": "crypto"},
]


def generate_backlink_report():
    """Generate a report of all backlink opportunities"""
    report = {
        "site": SITE_URL,
        "generated_at": datetime.now().isoformat(),
        "articles": len(ARTICLES),
        "social_bookmarks": len(SOCIAL_BOOKMARKS),
        "web20_platforms": len(WEB20_PLATFORMS),
        "directories": len(DIRECTORIES),
        "forums": len(FORUMS),
        "total_opportunities": len(SOCIAL_BOOKMARKS) + len(WEB20_PLATFORMS) + len(DIRECTORIES) + len(FORUMS),
        "articles_to_promote": ARTICLES,
        "social_bookmark_targets": SOCIAL_BOOKMARKS,
        "web20_targets": WEB20_PLATFORMS,
        "directory_targets": DIRECTORIES,
        "forum_targets": FORUMS,
    }
    return report


def generate_outreach_emails():
    """Generate outreach emails for guest posting"""
    templates = []
    
    # Template 1: Guest Post Request
    templates.append({
        "type": "guest_post",
        "subject": "Guest Post Submission: Best Crypto Casinos 2026",
        "body": f"""Hi there,

I'm reaching out because I love your content about crypto and online gambling. I have a well-researched article that I think your audience would find valuable:

"Best Crypto Casinos 2026 — Top 10 Bitcoin Gambling Sites Compared"

This comprehensive guide covers:
- Top 10 crypto casinos ranked by bonuses, games, and safety
- Detailed comparisons of Stake, BC.Game, BitStarz, and more
- Expert analysis of withdrawal speeds and security

I'd love to contribute this as a guest post on your site. In return, I can offer:
- A dofollow backlink to my site (affiliate99.netlify.app)
- Social media promotion of the published article
- A reciprocal link from my site to yours

Would you be interested? I can have the full article ready within 24 hours.

Best regards,
StakeReview Team
{SITE_URL}"""
    })

    # Template 2: Resource Page Link Request
    templates.append({
        "type": "resource_link",
        "subject": "Suggestion for Your Resources Page",
        "body": f"""Hi there,

I was browsing your site and noticed you have a great resources page. I wanted to suggest a resource that might be valuable for your visitors:

{SITE_URL}/blog/best-crypto-casinos-2026.html

This is our comprehensive guide to the best crypto casinos in 2026, featuring:
- Detailed reviews of 10 top crypto casinos
- Bonus comparisons
- Safety and security analysis
- Payment method breakdowns

It's regularly updated and provides genuine value to readers interested in crypto gambling.

Would you consider adding it to your resources? I'd be happy to reciprocate with a link from my site.

Best regards,
StakeReview Team"""
    })

    # Template 3: Broken Link Building
    templates.append({
        "type": "broken_link",
        "subject": "Broken Link on Your Site + Replacement Suggestion",
        "body": f"""Hi there,

I was reading an article on your site and noticed a broken link that used to point to a crypto casino comparison.

I have a similar resource that could be a good replacement:

{SITE_URL}/blog/stake-vs-bc-game.html

This is our detailed comparison of Stake Casino vs BC.Game, covering games, bonuses, payments, and more.

If you find it suitable, I'd appreciate you updating the broken link to point to my resource. It would be a win-win — your readers get a working link, and I get a quality backlink.

Thanks for considering!

Best regards,
StakeReview Team"""
    })

    return templates


def generate_social_posts():
    """Generate social media posts for backlinking"""
    posts = []
    
    for article in ARTICLES:
        posts.append({
            "platform": "Twitter/X",
            "text": f"📢 {article['title']}\n\n{article['description'][:100]}...\n\nRead more: {article['url']}\n\n#CryptoCasino #Bitcoin #Gambling #StakeCasino #BCGame"
        })
        posts.append({
            "platform": "Reddit",
            "title": article['title'],
            "text": f"{article['description']}\n\nFull article: {article['url']}"
        })
        posts.append({
            "platform": "Facebook",
            "text": f"🔥 {article['title']}\n\n{article['description']}\n\n👉 {article['url']}"
        })
    
    return posts


def generate_forum_posts():
    """Generate forum signature and post templates"""
    return [
        {
            "platform": "Bitcointalk",
            "signature": f"[url={SITE_URL}]StakeReview - Honest Crypto Casino Reviews[/url] | [url={SITE_URL}/bc-game-review.html]BC.Game Review[/url]",
            "post_template": f"""Hey everyone,

I've been researching crypto casinos extensively and put together some comprehensive reviews that might help:

- Stake Casino Review: {SITE_URL}
- BC.Game Review: {SITE_URL}/bc-game-review.html
- Best Crypto Casinos 2026: {SITE_URL}/blog/best-crypto-casinos-2026.html

All reviews are unbiased and based on real testing. Hope this helps anyone looking for a reliable crypto casino!

Cheers!"""
        },
        {
            "platform": "Reddit",
            "post_template": f"""I've been testing crypto casinos for a while and wrote up my findings:

**Best Crypto Casinos 2026:** {SITE_URL}/blog/best-crypto-casinos-2026.html

Covers Stake, BC.Game, BitStarz, mBit, and more. All tested for bonuses, games, withdrawals, and safety.

Hope this helps! Happy to answer any questions."""
        }
    ]


def main():
    """Main function - generate all backlink assets"""
    print("=" * 60)
    print("🔗 BACKLINK AUTOMATION REPORT")
    print("=" * 60)
    print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"🌐 Site: {SITE_URL}")
    print("=" * 60)
    
    # Generate report
    report = generate_backlink_report()
    print(f"\n📊 BACKLINK OPPORTUNITIES:")
    print(f"   Articles to promote: {report['articles']}")
    print(f"   Social bookmarking: {report['social_bookmarks']}")
    print(f"   Web 2.0 platforms: {report['web20_platforms']}")
    print(f"   Directories: {report['directories']}")
    print(f"   Forums: {report['forums']}")
    print(f"   TOTAL: {report['total_opportunities']} opportunities")
    
    # Generate outreach emails
    emails = generate_outreach_emails()
    print(f"\n📧 OUTREACH EMAILS GENERATED: {len(emails)}")
    for email in emails:
        print(f"   - {email['type']}: {email['subject']}")
    
    # Generate social posts
    social_posts = generate_social_posts()
    print(f"\n📱 SOCIAL POSTS GENERATED: {len(social_posts)}")
    
    # Generate forum posts
    forum_posts = generate_forum_posts()
    print(f"\n💬 FORUM TEMPLATES GENERATED: {len(forum_posts)}")
    
    # Save everything to JSON
    output = {
        "report": report,
        "outreach_emails": emails,
        "social_posts": social_posts,
        "forum_posts": forum_posts,
    }
    
    output_path = "C:\\Users\\goekh\\stake-affiliate-site\\backlink_strategy.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Full strategy saved to: {output_path}")
    print("\n" + "=" * 60)
    print("✅ BACKLINK AUTOMATION COMPLETE")
    print("=" * 60)
    
    return output


if __name__ == "__main__":
    main()
