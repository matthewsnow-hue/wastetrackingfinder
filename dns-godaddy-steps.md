# wastetrackingfinder.co.uk: GoDaddy DNS steps (for Matthew)

What's already done on GitHub (19 Oct 2026): the repo matthewsnow-hue/wastetrackingfinder publishes from `main` (root), the custom domain is set to `wastetrackingfinder.co.uk`, and the `CNAME` file is in the repo. The site stays hidden from search engines (noindex, robots.txt Disallow) until go-live.
Sources checked 19 Oct 2026:
- GitHub Pages IPs: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- Google Workspace MX: https://support.google.com/a/answer/174125
- Google SPF: https://support.google.com/a/answer/10685031

## 1. Open the DNS page
GoDaddy → My Products → wastetrackingfinder.co.uk → **DNS**.

## 2. Delete these first
| Type | Name | Value | What to do |
|---|---|---|---|
| A | @ | GoDaddy's parked address (shown as "Parked" or a GoDaddy IP) | Delete |
| CNAME | www | anything that isn't matthewsnow-hue.github.io (often `@`) | Delete (re-added in step 3) |
| MX | @ | any GoDaddy default mail record (e.g. `mailstore1.secureserver.net`, `smtp.secureserver.net`) | Delete |
| TXT | @ | any existing record starting `v=spf1` | Delete (a domain must have only one SPF record) |
| Forwarding | domain or subdomain | any | On the **Forwarding** tab, delete it |

Leave the NS and SOA records alone. Don't add any wildcard (`*`) record.

## 3. Add these records (copy exactly)
| Type | Name | Value | Priority | TTL |
|---|---|---|---|---|
| A | @ | 185.199.108.153 | | 1 Hour |
| A | @ | 185.199.109.153 | | 1 Hour |
| A | @ | 185.199.110.153 | | 1 Hour |
| A | @ | 185.199.111.153 | | 1 Hour |
| AAAA | @ | 2606:50c0:8000::153 | | 1 Hour |
| AAAA | @ | 2606:50c0:8001::153 | | 1 Hour |
| AAAA | @ | 2606:50c0:8002::153 | | 1 Hour |
| AAAA | @ | 2606:50c0:8003::153 | | 1 Hour |
| CNAME | www | matthewsnow-hue.github.io | | 1 Hour |
| MX | @ | smtp.google.com | 1 | 1 Hour |
| TXT | @ | v=spf1 include:_spf.google.com ~all | | 1 Hour |
| TXT | `_github-pages-challenge-matthewsnow-hue` | **PASTE FROM GITHUB** (step 4) | | 1 Hour |
| TXT | @ | **PASTE FROM GOOGLE ADMIN** (`google-site-verification=…`, step 5) | | 1 Hour |

Notes:
- The www value is just `matthewsnow-hue.github.io`, without `/wastetrackingfinder`.
- This SPF line must be the domain's only `v=spf1` record. It's fine for the SPF TXT and the Google verification TXT to both sit on `@`.

## 4. GitHub domain verification TXT (stops anyone else claiming the domain on GitHub)
1. GitHub → your profile picture → **Settings** → **Pages** → **Add a domain** → `wastetrackingfinder.co.uk` → **Add domain**.
2. GitHub shows a TXT name like `_github-pages-challenge-matthewsnow-hue` and a value that's unique to you. Paste both into the GitHub TXT row above.
3. Back on GitHub, click **Verify**. If it fails, wait 10–30 minutes and try again.

## 5. Google Workspace verification TXT
1. Google Admin console → add `wastetrackingfinder.co.uk` as a user alias domain (Account → Domains → Manage domains → Add a domain).
2. When it asks you to verify, choose the TXT record method and copy the `google-site-verification=…` value.
3. Paste it into the Google TXT row above (Name `@`), then press **Verify** in the Admin console.
4. Mail to hello@wastetrackingfinder.co.uk works once the alias domain is verified and the MX record has updated. hello@ still needs adding as an alias on a user, or as a group.

## 6. Once DNS resolves: switch on Enforce HTTPS
DNS changes often take minutes, but can take up to 24 hours.
1. GitHub → repo **matthewsnow-hue/wastetrackingfinder** → **Settings** → **Pages**. Under "Custom domain", you should see "DNS check successful".
2. Once the certificate is ready (up to 24 hours), tick **Enforce HTTPS**.
3. Check that https://wastetrackingfinder.co.uk shows the padlock and https://www.wastetrackingfinder.co.uk redirects to it.

## Optional, later: DKIM
Admin console → Apps → Google Workspace → Gmail → **Authenticate email** → pick the domain → **Generate new record** (2048-bit). Add the TXT it gives you (name `google._domainkey`) in GoDaddy, then click **Start authentication**. This improves delivery of mail you send from the domain.

Tell Tel once steps 3–5 are done. Tel can then do step 6 and run the checks.
