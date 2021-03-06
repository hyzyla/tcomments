import React, {FC} from "react";
import sanitizeHtml from 'sanitize-html'
import css from './PostCard.module.css';

const defaultOptions = {
  allowedTags: [ 'b', 'strong', 'i', 'em', 'u', 'ins', 's', 'strike', 'del', 'a', 'code', 'pre' ],
  allowedAttributes: {
    'a': [ 'href' ],
    'code': ['class'],

  },
  allowedIframeHostnames: ['www.youtube.com']
};

const sanitize = (dirty): string => {
  return sanitizeHtml(
      dirty,
      defaultOptions
    )
};

interface Props {
  html: string;
}

export const PostText: FC<Props> = ({ html }) => {
  const sanitized = sanitize(html).replace(/\n/g, "<br />");

  console.log(sanitized);
  return (
      <div className={css.paragraph} dangerouslySetInnerHTML={{__html: sanitized}} />
  );
};