# auto-update-audience-in-google-ads

## Usage

Automating to update the audience in Google Ads. The audiences are updated based on Google Analytics (GA, Universal Analytics) report. 

`Benefit of this strategy`: `Lift the performance of advertising` in Google Ads. Have a higher `(1) number of clicks` and `(2) conversion rate` in the display ads.

## The Strategy

1. Analyze Audience reports in GA. Find top-n interests and demographic factors.
2. Update the audience list in Ads based on the GA report.

GA report,
<img src="img\ga-report-1.png" style="zoom:50%;" />
<img src="img\ga-report-2.png" style="zoom:50%;" />

Update audience in Ad,
<img src="img\ads.jpg" style="zoom:50%;" />


### Steps of this program:

1. Get audience’s interests report from Google Analytics Report API.
2. Take top-3 interests from each category in `GA Audience --> Interest` report.
3. Find and enable relevant audiences (i.e. interests) in Ads. Pause the irrelevant audiences.
4. Check the status of the Ad group. Enable it if it is pasued, otherwisw no action to Ad group.

## Configuration on [xxx]


## Contributing

[xxx]

## License
[MIT](https://choosealicense.com/licenses/mit/)