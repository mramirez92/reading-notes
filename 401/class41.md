# React 4

## Dynamic Routes

"How to statically generate pages with dynamic routes using getStaticPaths": For example, we can use `getStaticPaths` in a blog post page to generate all possible routes based on the post ID: 

```Javascript
export async function getStaticPaths() {
  const posts = await getAllPosts(); // fetch all blog posts from API
  const paths = posts.map((post) => ({
    params: { id: post.id },
  }));
  return { paths, fallback: false };
}
```

-   "How to write getStaticProps to fetch the data for each blog post": For example, we can use `getStaticProps` in the same blog post page to fetch the specific data for each post, like this:

```Javascript
export async function getStaticProps({ params }) {
  const post = await getPostById(params.id); // fetch specific post from API
  return {
    props: { post },
  };
}
```  

- "How to render markdown using remark": For example, we can use `react-markdown` in the blog post page to render the Markdown content of the post, like this:
```Javascript
import ReactMarkdown from 'react-markdown';

function BlogPost({ post }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <ReactMarkdown>{post.content}</ReactMarkdown>
    </div>
  );
}

```

- "How to pretty-print date strings": For example, we can use `toLocaleDateString` to format a date in a user-friendly way, like this:

```JavaScript
function BlogPost({ post }) {
  const date = new Date(post.date);
  const formattedDate = date.toLocaleDateString();
  return (
    <div>
      <h1>{post.title}</h1>
      <p>Published on {formattedDate}</p>
    </div>
  );
}

```

- "How to link to a page with dynamic routes": For example, we can use `Link` to create a link to another blog post page with a dynamic route, like this:

```Javascript
import Link from 'next/link';

function BlogPost({ post }) {
  return (
    <div>
      <h1>{post.title}</h1>
      <Link href="/posts/[id]" as={`/posts/${post.id}`}>
        <a>Read more</a>
      </Link>
    </div>
  );
}

```

Dynamic routes allow us to create flexible and scalable applications that can handle a large number of different routes. However, we need to be careful to properly handle the case where a dynamic route does not exist, either by using the `fallback` option in `getStaticPaths`, or by implementing a custom 404 page.

## Deployment

- The easiest way to deploy Next.js to production is to use the **[Vercel](https://vercel.com/?utm_source=next-site&utm_medium=learnpages&utm_campaign=next-website)** platform developed by the creators of Next.js.
	- Vercel is a serverless platform for static and hybrid applications built to integrate with your headless content, commerce, or database.

1. Import repository to Vercel
2. Use default values or change them. Vercel automatically detects the Next.js app and chooses optimal building settings: 
			-    Project Name
			-   Root Directory
			-   Build Command
			-   Output Directory
			-   Development Command
3.  DONE! Deployment URLs will be provided. 

## Vercel Suggested Workflow
### Develop, Preview, Ship

We’ve just gone through the workflow we call **DPS**: **D**evelop, **P**review, and **S**hip.

-   **Develop**: We’ve written code in Next.js and used the Next.js development server running to take advantage of its hot reloading feature.
-   **Preview**: We’ve pushed changes to a branch on GitHub, and Vercel created a preview deployment that’s available via a URL. We can share this preview URL with others for feedback. In addition to doing _code reviews_, you can do _deployment previews_.
-   **Ship**: We’ve merged the pull request to `main` to ship to production.

## Things I want to know more about

100% I want to learn more about building dynamic routes, I feel like I missed something in class about this. Maybe it was the stress of the upcoming whiteboards. This is something I definitely need to revisit. 

## Resources

[Dynamic Routes](https://nextjs.org/learn/basics/dynamic-routes)

[Deployment](https://nextjs.org/learn/basics/deploying-nextjs-app)
