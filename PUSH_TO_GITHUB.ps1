#!/usr/bin/env powershell
# SkyWeaver.AI - GitHub Push Script
# ================================

# This script will push your project to GitHub
# Make sure you've created the repo on github.com first!

$repoName = "skyweaver-ai"
$username = "mdsuhail-dev"
$email = "suhailmirzag58@gmail.com"

Write-Host "🚀 SkyWeaver.AI GitHub Push" -ForegroundColor Cyan
Write-Host "============================`n" -ForegroundColor Cyan

Write-Host "ℹ️  BEFORE YOU RUN THIS:" -ForegroundColor Yellow
Write-Host "1. Go to https://github.com/new" -ForegroundColor White
Write-Host "2. Create repository named: $repoName" -ForegroundColor White
Write-Host "3. Choose 'Public'" -ForegroundColor White
Write-Host "4. Do NOT check 'Initialize with README'" -ForegroundColor White
Write-Host "5. Click Create`n" -ForegroundColor White

Write-Host "Ready? Press Enter to continue..." -ForegroundColor Yellow
Read-Host

Write-Host "`n🔧 Setting up remote and pushing...`n" -ForegroundColor Cyan

# Add remote
git remote add origin "https://github.com/$username/$repoName.git"

# Rename branch to main
git branch -M main

# Push to GitHub
Write-Host "📤 Pushing to GitHub..." -ForegroundColor Cyan
git push -u origin main

Write-Host "`n✅ DONE! Your project is on GitHub!" -ForegroundColor Green
Write-Host "📍 https://github.com/$username/$repoName`n" -ForegroundColor Green
