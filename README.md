# waow.tech

## setup

1. push this repo to github:
```bash
git remote add origin git@github.com:zzstoatzz/waow.tech.git
git push -u origin main
```

2. go to cloudflare dashboard → pages → create a project

3. connect to your github repo (zzstoatzz/waow.tech)

4. build settings:
   - framework preset: none
   - build command: (leave empty)
   - build output directory: `/`

5. click "save and deploy"

6. once deployed, go to the project → custom domains → add waow.tech

that's it. every push to main auto-deploys.
