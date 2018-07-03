for name in Germany Austria Belgium Bulgaria Croatia Czech_Republic Denmark Finland France Greece Hungary Ireland Italy Lithuania Malta Netherlands Poland Romania Slovakia Slovenia Spain Sweden United_Kingdom Portugal
do 
   ./rating_step1.sh ./"$name".csv 

   python rating_step2.py ./"$name"_moodys.csv > ./"$name"_moodys_ref.csv
   
   python rating_step3.py ./dates.csv ./"$name"_moodys_ref.csv > out.csv 
   mv out.csv ./"$name"_moodys_ref.csv
done
