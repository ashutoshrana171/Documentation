<p>The banner at the top of the backtest results page displays the performance statistics of your backtest.</p>

<img class='img-responsive' src="https://cdn.quantconnect.com/i/tu/runtime-statistics.png">

<p>The following table describes the runtime statistics:</p>

<?php
include(DOCS_RESOURCES."/glossary.php");
echo "
<table class='qc-table table'>
  <thead>
    <tr>
      <th style='width: 25%'>Statistic</th>
      <th style='width: 75%'>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PSR</td>
      <td>{$defintionByTerm['probabilistic sharpe ratio (PSR)']}</td>
    </tr>
    <tr>
      <td>Unrealized</td>
      <td>{$defintionByTerm['unrealized']}</td>
    </tr>
    <tr>
      <td>Fees</td>
      <td>{$defintionByTerm['total fees']}</td>
    </tr>
    <tr>
      <td>Net Profit</td>
      <td>{$defintionByTerm['net profit']['dollar-value']}</td>
    </tr>
    <tr>
      <td>Return</td>
      <td>{$defintionByTerm['net profit']['percent']}</td>
    </tr>
    <tr>
      <td>Equity</td>
      <td>{$defintionByTerm['equity']}</td>
    </tr>
    <tr>
      <td>Holdings</td>
      <td>{$defintionByTerm['holdings']}</td>
    </tr>
    <tr>
      <td>Volume</td>
      <td>{$defintionByTerm['volume']}</td>
    </tr>
    <tr>
      <td>Capacity</td>
      <td>{$defintionByTerm['capacity']}</td>
    </tr>
  </tbody>
</table>";

echo file_get_contents(DOCS_RESOURCES."/create-custom-runtime-statistic.html"); 
?>
