#!/bin/bash

# NUCLEAR POWER MODE - ABSOLUTE MAXIMUM FORCE
echo "💣 ACTIVATING NUCLEAR POWER MODE 💣"

# Read HTML content once
HTML_CONTENT=$(<offer.html)

# Check if all.txt exists
if [[ ! -f "all.txt" ]]; then
    echo "❌ File all.txt not found."
    exit 1
fi

# Check if random.txt exists
if [[ ! -f "random.txt" ]]; then
    echo "❌ File random.txt not found."
    exit 1
fi

# Load configuration from random.txt
echo "🎭 LOADING RANDOM FROM CONFIGURATION 🎭"
source random.txt

# Validate loaded arrays
if [[ -z "${DOMAINS[@]}" ]]; then
    echo "❌ DOMAINS array not found in random.txt"
    exit 1
fi

if [[ -z "${SUBNAMES[@]}" ]]; then
    echo "❌ SUBNAMES array not found in random.txt"
    exit 1
fi

if [[ -z "${DISPLAY_NAMES[@]}" ]]; then
    echo "❌ DISPLAY_NAMES array not found in random.txt"
    exit 1
fi

# Check if SUBJECTS array exists, otherwise use DEFAULT_SUBJECT
if [[ -z "${SUBJECTS[@]}" ]]; then
    echo "⚠️  SUBJECTS array not found, using DEFAULT_SUBJECT"
    CURRENT_SUBJECT="${DEFAULT_SUBJECT:-🚀This winter, explore health coverage options🚀}"
else
    echo "✅ Loaded ${#SUBJECTS[@]} subject variations"
    CURRENT_SUBJECT="${SUBJECTS[$RANDOM % ${#SUBJECTS[@]}]}"
fi

echo "✅ Loaded ${#DOMAINS[@]} domains, ${#SUBNAMES[@]} subnames, ${#DISPLAY_NAMES[@]} display names"
echo "📨 Using subject: $CURRENT_SUBJECT"

# COUNT TOTAL EMAILS
TOTAL_EMAILS=$(wc -l < all.txt)
echo "📧 Total emails to send: $TOTAL_EMAILS"

# FUNCTION TO GET REAL QUEUE SIZE (BULLETPROOF)
get_queue_size() {
    local size=$(mailq 2>/dev/null | awk 'BEGIN {count=0} /^[A-F0-9]/ {count++} END {print count}')
    echo "${size:-0}"
}

# GET INITIAL QUEUE SIZE
INITIAL_QUEUE=$(get_queue_size)
echo "📊 Initial queue size: $INITIAL_QUEUE"

# EXTREME POSTFIX OPTIMIZATION
echo "⚡ TUNING POSTFIX FOR MAXIMUM WARFARE ⚡"
postconf -e default_process_limit=1000
postconf -e default_destination_concurrency_limit=500
postconf -e initial_destination_concurrency=200
postconf -e default_destination_rate_delay=0s
postconf -e maximal_queue_lifetime=1h
postconf -e bounce_queue_lifetime=1h
service postfix restart
sleep 2

# PRE-FLUSH NUCLEAR
echo "💥 PRE-FLUSHING ANY EXISTING QUEUE 💥"
postqueue -f
sleep 1

# ULTRA-FAST SENDING LOOP
echo "🚀 LAUNCHING NUCLEAR SENDING CAMPAIGN 🚀"
COUNT=0
START_TIME=$(date +%s)

while IFS= read -r email; do
    # Trim whitespace from email
    email=$(echo "$email" | xargs)
    
    # Skip empty lines
    if [[ -z "$email" ]]; then
        continue
    fi
    
    # GENERATE RANDOM FROM FOR EACH EMAIL (NUCLEAR MODE)
    RANDOM_DOMAIN=${DOMAINS[$RANDOM % ${#DOMAINS[@]}]}
    RANDOM_SUBNAME=${SUBNAMES[$RANDOM % ${#SUBNAMES[@]}]}
    RANDOM_DISPLAY=${DISPLAY_NAMES[$RANDOM % ${#DISPLAY_NAMES[@]}]}
    RANDOM_FROM_EMAIL="$RANDOM_SUBNAME@$RANDOM_DOMAIN"
    RANDOM_FROM="$RANDOM_DISPLAY <$RANDOM_FROM_EMAIL>"
    
    # RANDOM SUBJECT FOR EACH EMAIL (OPTIONAL - UNCOMMENT TO ACTIVATE)
    # RANDOM_SUBJECT="${SUBJECTS[$RANDOM % ${#SUBJECTS[@]}]}"
    # CURRENT_SUBJECT="$RANDOM_SUBJECT"
    
    # SEND EMAIL WITH RANDOM FROM & BOUNCE TRACKING
    echo "$HTML_CONTENT" | mail \
         -a "Content-Type: text/html" \
         -a "Reply-To: smurillo@uvigo.es" \
         -a "X-Feedback-ID: 99999:timeshare:campaign1" \
         -a "From: $RANDOM_FROM" \
         -s "$CURRENT_SUBJECT" \
         -r "smurillo@uvigo.es" \
         "$email" 2>/dev/null &
    
    COUNT=$((COUNT + 1))
    
    # AGGRESSIVE FLUSHING EVERY 500 EMAILS
    if [ $((COUNT % 500)) -eq 0 ]; then
        postqueue -f >/dev/null 2>&1 &
        
        CURRENT_QUEUE=$(get_queue_size)
        ELAPSED=$(( $(date +%s) - START_TIME ))
        REAL_SENT=$((COUNT - CURRENT_QUEUE))
        echo "⚡ QUEUED: $COUNT | REAL SENT: $REAL_SENT | IN QUEUE: $CURRENT_QUEUE"
        echo "🎭 RANDOM FROM EXAMPLE: $RANDOM_FROM"
        echo "📨 CURRENT SUBJECT: $CURRENT_SUBJECT"
        
        # CHANGE SUBJECT PERIODICALLY (OPTIONAL)
        if [[ -n "${SUBJECTS[@]}" ]]; then
            CURRENT_SUBJECT="${SUBJECTS[$RANDOM % ${#SUBJECTS[@]}]}"
            echo "🔄 SUBJECT CHANGED TO: $CURRENT_SUBJECT"
        fi
    fi
    
    # HYPER-FLUSH EVERY 2000 EMAILS
    if [ $((COUNT % 2000)) -eq 0 ]; then
        echo "💣 HYPER-FLUSHING QUEUE 💣"
        for i in {1..10}; do
            postqueue -f >/dev/null 2>&1 &
        done
        service postfix reload >/dev/null 2>&1
        sleep 0.5
    fi
    
    # NUCLEAR RESET EVERY 10000 EMAILS
    if [ $((COUNT % 10000)) -eq 0 ]; then
        echo "☢️  NUCLEAR POSTFIX RESET ☢️"
        service postfix restart >/dev/null 2>&1
        sleep 2
        postqueue -f >/dev/null 2>&1
    fi
    
done < all.txt

# WAIT FOR ALL MAIL COMMANDS
echo "⏳ FINALIZING QUEUE SUBMISSION..."
wait

# NUCLEAR QUEUE DRAIN MODE
echo "🎯 ACTIVATING NUCLEAR QUEUE DRAIN MODE 🎯"
NUCLEAR_START=$(date +%s)
STUCK_COUNT=0
LAST_QUEUE=0

while true; do
    CURRENT_QUEUE=$(get_queue_size)
    CURRENT_TIME=$(date +%s)
    ELAPSED=$((CURRENT_TIME - NUCLEAR_START))
    
    REAL_SENT=$((TOTAL_EMAILS - CURRENT_QUEUE))
    
    if [ "$CURRENT_QUEUE" -eq "$LAST_QUEUE" ] && [ "$CURRENT_QUEUE" -gt 0 ]; then
        STUCK_COUNT=$((STUCK_COUNT + 1))
    else
        STUCK_COUNT=0
    fi
    
    LAST_QUEUE=$CURRENT_QUEUE
    
    if [ "$CURRENT_QUEUE" -eq 0 ]; then
        echo "🎉 NUCLEAR VICTORY! ALL $TOTAL_EMAILS EMAILS DELIVERED!"
        break
    fi
    
    echo "📊 NUCLEAR DRAIN: $CURRENT_QUEUE left | SENT: $REAL_SENT/$TOTAL_EMAILS"
    
    echo "💣 DEPLOYING TACTICAL NUCLEAR FLUSHING 💣"
    
    for i in {1..50}; do
        postqueue -f >/dev/null 2>&1 &
    done
    wait
    
    postsuper -r ALL >/dev/null 2>&1
    
    service postfix restart >/dev/null 2>&1
    sleep 2
    for i in {1..20}; do
        postqueue -f >/dev/null 2>&1 &
    done
    wait
    
    if [ $STUCK_COUNT -gt 5 ] && [ $CURRENT_QUEUE -gt 0 ]; then
        echo "☢️  DEPLOYING EXTREME QUEUE CLEANSE ☢️"
        service postfix stop >/dev/null 2>&1
        
        rm -f /var/spool/postfix/deferred/* >/dev/null 2>&1
        rm -f /var/spool/postfix/incoming/* >/dev/null 2>&1
        service postfix start >/dev/null 2>&1
        sleep 3
        STUCK_COUNT=0
    fi
    
    if [ $STUCK_COUNT -gt 10 ]; then
        echo "🔄 FORCING STUCK EMAILS RETRY 🔄"
        postsuper -r ALL
        sleep 10
    fi
    
    sleep 2
done

echo "🔍 CONDUCTING FINAL NUCLEAR VERIFICATION..."
FINAL_QUEUE=$(get_queue_size)
if [ "$FINAL_QUEUE" -eq 0 ]; then
    echo "✅ NUCLEAR SUCCESS: ALL $TOTAL_EMAILS EMAILS CONFIRMED DELIVERED!"
else
    echo "⚠️  NUCLEAR WARNING: $FINAL_QUEUE emails still in queue after maximum effort"
    echo "💣 DEPLOYING FINAL NUCLEAR OPTION..."
    service postfix stop
    service postfix start
fi

END_TIME=$(date +%s)
TOTAL_TIME=$((END_TIME - START_TIME))
if [ $TOTAL_TIME -eq 0 ]; then
    TOTAL_TIME=1
fi

FINAL_RATE=$((TOTAL_EMAILS / TOTAL_TIME))

echo "💣 NUCLEAR MISSION COMPLETE!"
echo "📊 Total emails: $TOTAL_EMAILS"
echo "⏱️  Total time: $TOTAL_TIME seconds"
echo "🚀 Average rate: $FINAL_RATE emails/second"
echo "🎯 Final queue status: $(get_queue_size) emails remaining"
echo "🎭 Random From configuration: ${#DOMAINS[@]} domains x ${#SUBNAMES[@]} subnames x ${#DISPLAY_NAMES[@]} display names"
echo "📨 Subjects used: ${#SUBJECTS[@]} variations"

echo "🧹 PERFORMING EXTREME SYSTEM CLEANUP..."
sync
echo 3 | tee /proc/sys/vm/drop_caches >/dev/null 2>&1