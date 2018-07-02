for name in Germany Austria Belgium Bulgaria Croatia Czech_Republic Denmark Finland France Greece Hungary Ireland Italy Lithuania Malta Netherlands Poland Romania Slovakia Slovenia Spain Sweden United_Kingdom
do 
   python ./unify.py ./Portugal.csv ./"$name".csv > "$name"_ref.csv
done
