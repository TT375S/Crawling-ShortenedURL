cd ~/git/Crawling-ShortenedURL/bruteForce



while true;
do
    echo "bitly";
    cat ./bitly/`ls -1 -t ./bitly | head -n 1 ` | wc -l;
    echo "isgd";
    cat ./isgd/`ls -1 -t ./isgd | head -n 1 ` | wc -l;
    echo "tinyurl";
    cat ./tinyurl/`ls -1 -t ./tinyurl | head -n 1 ` | wc -l;
    echo "prtnu";
    cat ./prtnu/`ls -1 -t ./prtnu | head -n 1 ` | wc -l;
    echo "owly";
    cat ./owly/`ls -1 -t ./owly | head -n 1 ` | wc -l;
    echo "tco";
    cat ./tco/`ls -1 -t ./tco | head -n 1 ` | wc -l;
    #echo "googl";
    #cat ./googl/`ls -1 -t ./googl | head -n 1 ` | wc -l;

    sleep 5m;
done
