from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import smtplib
def send_email(message, subject_message):
    try:
        msg = MIMEMultipart()
        part2 = MIMEText(message, 'html')
        msg.attach(part2)
        msg['Subject'] = subject_message
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.login('krishnaajay998@gmail.com', 'vjhjtzwvploqraew')
        recipients = ['ajay.krishna@quintetsolutions.com', 'krishnaajay998@gmail.com']
        msg["To"] = ",".join(recipients)
        bcc = ['krishnaajay998@gmail.com', 'ajay.krishna@quintetsolutions.com']
        to_address = recipients + bcc
        server.sendmail('krishnaajay998@gmail.com', to_address, msg.as_string())
        print("Alert mail sent successfully")
    except Exception as e:
        print("Unable to send email due to the loss of network: "+str(e))

message = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" style="background-color: #f3f3f3; min-height: 100%;">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Work Order</title>

</head>

<body bgcolor="#eeeeee" style="-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; box-sizing: border-box; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0; min-width: 100%; padding: 0; text-align: left; width: 100% !important;">

<table class="body" data-made-with-foundation="" style="border-collapse: collapse; border-spacing: 0; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; height: 100%; line-height: 1.3; margin: 0; padding: 0; text-align: left; vertical-align: top; width: 100%;" bgcolor="#f3f3f3">
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td class="float-center" align="center" valign="top" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; float: none; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0 auto; padding: 0; word-wrap: break-word;">
      <table class="container" align="center" style="border-collapse: collapse; border-spacing: 0; margin: 0 auto; padding: 0; text-align: inherit; vertical-align: top; width: 580px;" bgcolor="#fefefe">
        <tr style="padding: 0; vertical-align: top;" align="left">
          <td class="vendor-email-body-wrapper" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 10px 25px; word-wrap: break-word;" align="left" valign="top">

              <table class="row" style="border-collapse: collapse; border-spacing: 0; display: table; padding: 0; position: relative; text-align: left; vertical-align: top; width: 100%;">
    <tr style="padding: 0; vertical-align: top;" align="left">
      <th height="70" valign="middle" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0; padding: 0;" align="left">
        <img class="logo" alt="Company Logo" src="https://images.cdn.appfolio.com/areg/images/1722decf-2ac1-4ec7-919d-0ad48f6a97fa/large.png" style="-ms-interpolation-mode: bicubic; clear: both; display: block; max-height: 60px; max-width: 200px; outline: none; padding-left: 10px; padding-right: 10px; text-decoration: none; width: auto;">
      </th>
    </tr>
  </table>
  <table class="spacer" style="border-collapse: collapse; border-spacing: 0; padding: 0; text-align: left; vertical-align: top; width: 100%;">
    <tbody>
    <tr style="padding: 0; vertical-align: top;" align="left">
      <td height="15px" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; mso-line-height-rule: exactly; padding: 0; word-wrap: break-word;" align="left" valign="top"></td>
    </tr>
    </tbody>
  </table>
<table class="row" style="border-collapse: collapse; border-spacing: 0; display: table; padding: 0; position: relative; text-align: left; vertical-align: top; width: 100%;">
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 0; word-wrap: break-word;" align="left" valign="top">
      <p class="js-name" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0 0 10px; padding: 0;" align="left">Hello Lula- Smarter Property Maintenance,</p>
      <p class="js-reminder-statement" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0 0 10px; padding: 0; white-space: pre-line;" align="left">You have been assigned a work order in Overland Park, KS 66214. Please review and accept or reject it by 12:55 PM CST.</p>
    </td>
  </tr>
</table>
<table class="spacer" style="border-collapse: collapse; border-spacing: 0; padding: 0; text-align: left; vertical-align: top; width: 100%;">
  <tbody>
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td height="10px" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; mso-line-height-rule: exactly; padding: 0; word-wrap: break-word;" align="left" valign="top"></td>
  </tr>
  </tbody>
</table>
  <table class="row" style="border-collapse: collapse; border-spacing: 0; display: table; padding: 0; position: relative; text-align: left; vertical-align: top; width: 100%;">
    <tr style="padding: 0; vertical-align: top;" align="left">
      <td align="center" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 0; word-wrap: break-word;" valign="top">
        <table style="border-collapse: collapse; border-spacing: 0; padding: 0; text-align: left; vertical-align: top;">
          <tr style="padding: 0; vertical-align: top;" align="left">
            <td class="action-button" bgcolor="009cf7" height="30" width="275" align="center" valign="middle" style="-moz-border-radius: 3px; -ms-hyphens: auto; -webkit-border-radius: 3px; -webkit-hyphens: auto; border-collapse: collapse !important; border-radius: 3px; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 1em; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 0; word-wrap: break-word;">
              <a class="action-button__link scrub-href" href="https://sg.appfolio.com/ls/click?upn=SEmYLt35t2PsBK7zrZwyvHbpIwYmxl3AHlcKVr0mL-2B2dO9bi7nMyz-2FjQWGzVb6uY-2Bovc-2BiXhQH9bb-2FvPK9yiBsFWBo3f1d6xELTQzuibzZhE4k5gJ1RVScQawn6ZujRCTuDtoWOPaAB1BZWLaLd50BJnHBRK2d1ANL3Sp9bnCbtsoWKOJp6s9o7kgn9aqgi-2F2aMt9nGwqpNiLfJ-2BlsTooVYj7GYo772ftJBiA9oFw1fr4LVK9gzb-2F5XjljxUqiLPqnk0LK3jrcf-2FimApAwzWkFJI8Mf-2FaZqMKE-2BXkVS4W5lqElNxzOExThplht-2BhGP5x2tPjqKNUcGkfHwMWmSF6dOTdcPjscLX9-2Fp2nOJPDbupDquAoVsd4j9zv9aHNFDWFV-2BaFrdaad4CRAQ5mx6ss-2BT0rsYbugzx3WXlHd0HB6ZY2sPdIsaOJAnTV1lRsXSfN6Ho55EQnGkecpBdlfZmgI2NXYAKW7bHpVYMEzMZ7SWIUoPsxNGZU0jWUysCmI2soTYRwOJ4NfWlVKPVFn3FCaRRQVpUn29rI-2B9IOMPQi02irfkMKbLwE6-2BCrO0AdeVdiIDWyaL9cqmT9-2B1AQfsYk2WLkctW4kYbvVD1VS2ymw5H3BInNFngzwdas8J-2BAbZUXlJkFSF7Xntg0cdcsAuiCuTq-2B-2FZLpV0X2ffi1oeGjFX5SLmusEDR3zdxeRz1-2Fh3CA1febin-2B9f4TYA-2F0MUz7i73DaXADMrGtcOATM3vAS1huI-2Bdslxm9tDiFPbDMZsGq3hW3GIRPOVahBjL1lRY6aehAplRYciesJV-2BrZ6H5VPHJKJL-2BNtTo7bbRVwPkBHy7wJOeUyyIxSrJOBVJzf149NdnB9ahXWAk1tObhNK2cyjoxo0O1lL57q3IcvCbijjvDKxIqAKaqEQZk12I7A2sViKJkkGQ8Pc52p6CRdCjJhk681errP39Oq4v4dA9g617RLnz5K0CKfX74gTpCWun6rIMt9sUfxTji-2BIYdPvPzjwnz7h4Dfa62QcWMJJDMj6P-2BBgG9HSlu5RPuj0zp5WL40tIfJKE50QUI67qgdwavORZ6-2BOzbk9kmqtElJ3COCpEqvBecK6Bgq0usTjFQ1Ch-2BmNU1sjVPkCwNdyhzxX-2F7Kq6Iv67W-2BFrde0xjR29WoOPWS5AT6DiyrZM1ZnLlwBML0g-3D-3DeAOp_kuX2cI8baDAaOcj-2Fp3iIjU6R7PXKa3dAYAr0B7iMyKwz-2FaV0nnIuCVP1pcf8DEy1rdfWqpzAQNZA1Y921B94NoDVp98Z02ebQDwPOviJIcmHJ5zthc0Mn-2Ffwj8SQXtjMdOaGkplu2FKJMCiPSJ5nFnfQ88QDTkk61H-2Fa4KxWu7JH85HqfJI13Gpu9-2BRpKknyUyGAkWsmV0-2BK8IQ7eAo1NOuahZVuxiBdJlV4g83vluVH8inQjvJjyvmocEuCaHF111Cq8cg3eMjoDx0xmpphQQh-2Fz5JP3YxFGxZjzfkEtdjBVFTPkbwoHCSw-2FjFl-2BRcklFGDHuhDydBINqYNxevQat6vw8ASRfGFdh-2BCW069XsIOiDpjZyilTwjlly-2FNe7KoP2CZvMVSkwOiZ3X6ZxL90MFrY-2B3Rfjvdq59cTi74F1KcAaPB8GRjlfQ4f9UACaPB-2FerLsofBAlv0wluEyJob-2Fw-3D-3D" style="color: #ffffff !important; display: block !important; font-family: Helvetica, Arial, sans-serif; font-size: 1.1em; font-weight: normal; line-height: 1.3; margin: 0; padding: 11px 5px; text-align: center; text-decoration: none;">View Work Order</a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
<table class="spacer" style="border-collapse: collapse; border-spacing: 0; padding: 0; text-align: left; vertical-align: top; width: 100%;">
  <tbody>
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td height="15px" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; mso-line-height-rule: exactly; padding: 0; word-wrap: break-word;" align="left" valign="top"></td>
  </tr>
  </tbody>
</table>
<table class="row" style="border-collapse: collapse; border-spacing: 0; display: table; padding: 0; position: relative; text-align: left; vertical-align: top; width: 100%;">
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 0; word-wrap: break-word;" align="left" valign="top">
      <p class="js-thank-you" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0 0 10px; padding: 0;" align="left">Let us know if you have any questions.</p>
    </td>
  </tr>
</table>
<table class="spacer" style="border-collapse: collapse; border-spacing: 0; padding: 0; text-align: left; vertical-align: top; width: 100%;">
  <tbody>
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td height="15px" style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; mso-line-height-rule: exactly; padding: 0; word-wrap: break-word;" align="left" valign="top"></td>
  </tr>
  </tbody>
</table>
<table class="row" style="border-collapse: collapse; border-spacing: 0; display: table; padding: 0; position: relative; text-align: left; vertical-align: top; width: 100%;">
  <tr style="padding: 0; vertical-align: top;" align="left">
    <td style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 0; word-wrap: break-word;" align="left" valign="top">
      <p class="js-company-name" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0 0 10px; padding: 0;" align="left">Zach Hall</p>
        <p class="js-company-phone-number" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0 0 10px; padding: 0;" align="left">
          <a href="tel:(303)%20242-8980" style="-ms-hyphens: none; -ms-word-break: break-all; -webkit-hyphens: none; color: #32a98e; font-family: Helvetica, Arial, sans-serif; font-weight: normal; hyphens: none; line-height: 1.3; margin: 0; overflow-wrap: break-word; padding: 0; text-align: left; text-decoration: underline; word-break: break-word; word-wrap: break-word;">
            (303) 242-8980
          </a>
        </p>
        <p class="js-company-website" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0 0 10px; padding: 0;" align="left">
          <a target="_blank" href="https://sg.appfolio.com/ls/click?upn=RtZIZfCRUEBqytGWSZyvfh4yKo3Hnxf4BxJQ8uDJpX4-3Dkh8A_kuX2cI8baDAaOcj-2Fp3iIjU6R7PXKa3dAYAr0B7iMyKwz-2FaV0nnIuCVP1pcf8DEy1rdfWqpzAQNZA1Y921B94NoDVp98Z02ebQDwPOviJIcmHJ5zthc0Mn-2Ffwj8SQXtjMdOaGkplu2FKJMCiPSJ5nFnfQ88QDTkk61H-2Fa4KxWu7JH85HqfJI13Gpu9-2BRpKknyUyGAkWsmV0-2BK8IQ7eAo1NOuahZVuxiBdJlV4g83vluVH8inQjvJjyvmocEuCaHF111Cq8cg3eMjoDx0xmpphQVD-2FPntn3WFXTZMVroNdRk0DrrRnv9cJblesjf9BRFgBupea5kouc0ZHfDJOR7Rk-2FU3r834vC0HqN47AtPFJFCjvFIRFCCAfOfeS8L8F8aZc1ch6tpYrsj8OZKFphdKQU-2FZeaXH8n6YVA1SlFT-2F-2FDj10tD3bWxAGXU-2BRD4yYUDwELo7pwhBTnrhJ7f-2BXpdRhgA-3D-3D" style="-ms-hyphens: none; -ms-word-break: break-all; -webkit-hyphens: none; color: #32a98e; font-family: Helvetica, Arial, sans-serif; font-weight: normal; hyphens: none; line-height: 1.3; margin: 0; overflow-wrap: break-word; padding: 0; text-align: left; text-decoration: underline; word-break: break-word; word-wrap: break-word;">www.realatlas.com</a>
        </p>
    </td>
  </tr>
</table>


          </td>
        </tr>
      </table>

      <table class="container" align="center" style="border-collapse: collapse; border-spacing: 0; margin: 0 auto; padding: 0; text-align: inherit; vertical-align: top; width: 580px;" bgcolor="#fefefe">
        <tr style="padding: 0; vertical-align: top;" align="left">
          <td style="-ms-hyphens: auto; -webkit-hyphens: auto; border-collapse: collapse !important; color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; hyphens: auto; line-height: 1.3; margin: 0; padding: 0; word-wrap: break-word;" align="left" valign="top">
            <table class="row" style="border-collapse: collapse; border-spacing: 0; display: table; padding: 0; position: relative; text-align: left; vertical-align: top; width: 100%;">
              <tr style="padding: 0; vertical-align: top;" align="left">
                <th height="70" valign="middle" bgcolor="#545454" style="color: #0a0a0a; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: normal; line-height: 1.3; margin: 0; padding: 0;" align="left">
                  <img alt="Appfolio" class="float-end logo" style="-ms-interpolation-mode: bicubic; clear: both; display: block; height: 60%; max-height: 60px; max-width: 200px; outline: none; padding-left: 10px; padding-right: 10px; text-decoration: none; width: auto;" src="https://public.cdn.appfolio.com/public/images/af-white.png">
                </th>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>


<img src="https://sg.appfolio.com/wf/open?upn=Mhr-2FicLNYzVm-2Byh5riZVRTYrWWEbZ93Mq8I60rF5UL-2B7XKzLejhqmDdEVaUDizsOq-2BNvVlxYjHO1g2vEFa4IGZPPZPWSekftHzLNpSkvZ3WNxw1xCmOEKqTp6qcwaLFn-2BGwc1rXz8RwCWxPWWHlTNAZFHsAnvi4A6fQ9AR5FmMxse4wLEzRdOrijsA1IS2pGNBKVEYgiZ4lcOPKdfj82kB5-2BVFsi9XnixuyVOcl-2FKwqCXvGNiLdxmWiRJ6N27sTXw6FL8FuAQeay83p4cSFsN-2FnjYv4QhrNLacqcbyWNAgp0LA092ocFug0e1W9tj8OOpkcSc0YiZCi03Vj6jiS1Lflylq25sSyJNLITPIYj1LeNfy3WYRlkLvjqbWK-2FP-2BcL1dInhsRfbeKMYShyFmxkI7tzWp1YvgGAbafrJTUATtXyQ7bh1dgf3u-2B9iZM-2F-2F-2FiN-2BUXRAepW9ch3owL4OgcUWA-3D-3D" alt="" width="1" height="1" border="0" style="height:1px !important;width:1px !important;border-width:0 !important;margin-top:0 !important;margin-bottom:0 !important;margin-right:0 !important;margin-left:0 !important;padding-top:0 !important;padding-bottom:0 !important;padding-right:0 !important;padding-left:0 !important;"/></body>
</html>
"""
subject_message = "Appfolio: Alert: New Job found subject: Work Order #242315 - 1 | Zach Hall"
send_email(message,subject_message)
