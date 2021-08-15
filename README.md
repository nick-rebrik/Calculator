# Cash & Calories calculator
A calorie / finance calculator that helps you keep track of the balance of your funds or calories before consumption.

To get started with the calculator, create a class object with a limit of funds / calories:
<ul>
  <li><code>CashCalculator(Calculator)</code> - for finance calculator</li>
  <li><code>CaloriesCalculator(Calculator)</code> - for calorie calculator</li>
</ul>

<i><b>Common functionality of calculators:</i></b>
<ul>
  <li>Add a new record of spending or consuming calories - <code>add_record()</code></li>
  <li>Calculate the consumption of funds / calories for today - <code>get_today_stats()</code></li>
  <li>Calculate the consumption of funds / calories for the last week - <code>get_week_stats()</code>
</ul>

<i><b>Finance calculator can:</i></b>
<ul>
  <li><code>get_today_cash_remained(currency)</code> - Determines the balance and accepts the argument of one of the three available currencies:
    <ul>
      <li><i><b>Euro</b></i> - <code>'eur'</code></li>
      <li><i><b>Dollars</b></i> - <code>'usd'</code></li>
      <li><i><b>Ruble</b></i> - <code>'rub'</code></li>
    </ul>
  </li>       
</ul>

<i><b>Calorie calculator can:</i></b>
<ul>
  <li>Calculate how many calories you can still consume today - <code>get_calories_remained()</code></li>
</ul>

