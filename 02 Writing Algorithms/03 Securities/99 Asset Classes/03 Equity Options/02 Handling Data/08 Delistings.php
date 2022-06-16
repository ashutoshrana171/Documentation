<p>When a contract expires, LEAN adds a <code>Delisting</code> object to the <code>Slice</code> and liquidates your holdings. <code>Delisting</code> objects have the following properties:</p>

<div data-tree="QuantConnect.Data.Market.Delisting"></div>

<p>To get the <code>Delisting</code> objects, loop through the <code>Delistings</code> property of the <code>Slice</code>.</p>

<div class="section-example-container">
    <pre class="csharp">// Example of looping through Delistings</pre>
    <pre class="python"># Example of looping through Delistings</pre>
</div>