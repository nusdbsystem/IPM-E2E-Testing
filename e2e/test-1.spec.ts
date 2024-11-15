import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://137.132.92.226:4001/login');
});