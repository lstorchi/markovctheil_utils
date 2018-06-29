if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit
fi

basename=${1%.*}

grep "Moody's" $1 > $basename"_moodys.csv"
grep "S&P" $1 > $basename"_sep.csv"
grep "Fitch" $1 > $basename"_fitch.csv"
